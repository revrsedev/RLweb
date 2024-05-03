from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.conf import settings

class Podcast(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='podcasts/images/')
    artist_image = models.ImageField(upload_to='podcasts/artists/', default='media/default/default.webp')
    start_time = models.TimeField(default='12:00')
    end_time = models.TimeField(default='13:00')
    day_of_week = models.IntegerField(choices=[
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
        (6, 'Sunday'),
    ],default=0)
    poster = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='podcasts', null=True)

    def __str__(self):
        return self.title

class PodcastCreateView(CreateView):
    model = Podcast
    fields = ['title', 'image', 'artist_image', 'start_time', 'end_time', 'day_of_week']

    def form_valid(self, form):
        form.instance.poster = self.request.user 
        return super().form_valid(form)

class LiveShow(models.Model):
    title = models.CharField(max_length=200)
    dj_name = models.CharField(max_length=100)
    live_status = models.BooleanField(default=False)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.title} ({'live' if self.live_status else 'auto'})"

class RadioSettings(models.Model):
    stream_url = models.URLField()

    def __str__(self):
        return "Radio Settings"
    
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog_images/')
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title