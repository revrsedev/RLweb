from django.urls import path
from .views import home, about, schedule, blog, blog_details, show_details, radio_jockey, jockey_details, faq, sponsor, contact, live_shows, previous_shows, upcoming_shows, subscribe, podcast_schedule
from django.conf import settings
from django.conf.urls.static import static
from . import views

app = 'radio'

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('schedule/', schedule, name='schedule'),
    path('blog/', blog, name='blog'),
    path('blog/<int:post_id>/', views.blog_details, name='blog_details'),
    path('show_details/', show_details, name='show_details'),
    path('radio_jockey/', radio_jockey, name='radio_jockey'),
    path('jockey_details/', jockey_details, name='jockey_details'),
    path('faq/', faq, name='faq'),
    path('sponsor/', sponsor, name='sponsor'),
    path('contact/', contact, name='contact'),
    path('live_shows/', live_shows, name='live_shows'),
    path('previous_shows/', previous_shows, name='previous_shows'),
    path('upcoming_shows/', upcoming_shows, name='upcoming_shows'),
    path('subscribe/', subscribe, name='subscribe'),
    path('podcast_schedule/', podcast_schedule, name='podcast_schedule'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
