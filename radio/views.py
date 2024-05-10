from django.templatetags.static import static
from .models import Podcast, RadioSettings, LiveShow, BlogPost, Comment, Post, Category, Tag, DJ
from django.shortcuts import render, get_object_or_404, render, redirect
from .forms import CommentForm


def home(request):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    podcasts_by_day = {day: Podcast.objects.filter(day_of_week=days.index(day)) for day in days}
    live_show = LiveShow.objects.filter(live_status=True).first()
    radio_settings = RadioSettings.objects.first()
    djs = DJ.objects.all()
    
    if not live_show:
        live_show = {
            'title': 'Auto DJ',
            'dj_name': 'Automated Stream',
            'start_time': '00:00',
            'end_time': '23:59',
            'live_status': True,
            'stream_url': radio_settings.stream_url if radio_settings else 'https://ritmolatinoscs.radioca.st/stream',
            'image_url': static('images/shows/player/1.jpg'),
            'is_auto': True
        }
    else:
        live_show.is_auto = False
        live_show.stream_url = radio_settings.stream_url if radio_settings else 'https://ritmolatinoscs.radioca.st/stream'
        if hasattr(live_show, 'dj_image') and live_show.dj_image:
            live_show.image_url = live_show.dj_image.url
        else:
            live_show.image_url = static('images/shows/player/1.jpg')

    context = {
        'podcasts_by_day': podcasts_by_day,
        'live_show': live_show,
        'djs': djs
    }

    return render(request, 'radio/home.html', context)

def about(request):
    return render(request, 'radio/about.html')

def schedule(request):
    return render(request, 'radio/showShudle.html')

def blog(request):
    posts = BlogPost.objects.all()
    categories = Category.objects.all()
    return render(request, 'radio/blog_section.html', {'posts': posts, 'categories': categories})

def blog_details(request, post_id):  # Ensure only one definition exists
    post = get_object_or_404(BlogPost, pk=post_id)
    comments = post.comments.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect('radio:blog_details', post_id=post.id)

    context = {
        'post': post,
        'comments': comments,
        'categories': categories,
        'tags': tags,
        'form': form
    }
    return render(request, 'radio/blog_details_section.html', context)


def post_comment(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect('radio:blog_details', post_id=post_id)  # Assuming you have a view that shows blog details
    else:
        form = CommentForm()
    return redirect('radio:blog_details', post_id=post_id)

def category_detail(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    posts = BlogPost.objects.all()  # Adjust based on related name or direct query
    return render(request, 'radio/category_detail.html', {'category': category, 'posts': posts})

def dj_detail(request, dj_id):
    dj = get_object_or_404(DJ, id=dj_id)
    return render(request, 'radio/jockey-details.html', {'dj': dj})

def radio_jockey(request):
    djs = DJ.objects.all()  # Retrieve all DJ entries from the database
    return render(request, 'radio/radio-jockey.html', {'djs': djs})

def show_details(request):
    return render(request, 'radio/showDetails.html')

def faq(request):
    return render(request, 'radio/faq.html')

def sponsor(request):
    return render(request, 'radio/sponsor.html')

def contact(request):
    return render(request, 'radio/contact.html')

def live_shows(request):
    return render(request, 'radio/liveShows.html')

def previous_shows(request):
    return render(request, 'radio/previous_shows_section.html')

def upcoming_shows(request):
    return render(request, 'radio/rj_live_show_section.html')

def subscribe(request):
    return render(request, 'radio/subscribe_section.html')

def podcast_schedule(request):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    podcasts_by_day = {day: Podcast.objects.filter(day_of_week=days.index(day)) for day in days}
    return render(request, 'radio/podcast_schedule.html', {'podcasts_by_day': podcasts_by_day})
