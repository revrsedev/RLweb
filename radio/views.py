from django.shortcuts import render
from django.templatetags.static import static
from .models import Podcast, RadioSettings, LiveShow, BlogPost as Blog
from django.shortcuts import render, get_object_or_404


def home(request):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    podcasts_by_day = {day: Podcast.objects.filter(day_of_week=days.index(day)) for day in days}
    live_show = LiveShow.objects.filter(live_status=True).first()
    radio_settings = RadioSettings.objects.first()

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
        'live_show': live_show
    }

    return render(request, 'radio/home.html', context)



def about(request):
    return render(request, 'radio/about.html')

def schedule(request):
    return render(request, 'radio/showShudle.html')

def blog(request):
    posts = Blog.objects.all()  # This should reference Blog if it's the model you intend to use
    return render(request, 'radio/blog_section.html', {'posts': posts})

def blog_details(request, blog_id):
    post = get_object_or_404(Blog, id=blog_id)  # Again, make sure Blog is the correct model
    return render(request, 'radio/blog_details.html', {'post': post})

def blog_details(request):
    return render(request, 'radio/blog_details.html')

def show_details(request):
    return render(request, 'radio/showDetails.html')

def radio_jockey(request):
    return render(request, 'radio/djDetails.html')

def jockey_details(request):
    return render(request, 'radio/radioDetails.html')

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
