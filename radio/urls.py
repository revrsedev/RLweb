from django.urls import path
from .views import home, about, schedule, blog, show_details, faq, sponsor, contact, live_shows, previous_shows, upcoming_shows, subscribe, podcast_schedule, category_detail, dj_detail, radio_jockey, webchat
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'radio'

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('schedule/', schedule, name='schedule'),
    path('blog/', blog, name='blog'),
    path('blog/<int:post_id>/', views.blog_details, name='blog_details'),
    path('blog/<int:post_id>/comment/', views.post_comment, name='post_comment'),
    path('category/<slug:category_slug>/', views.category_detail, name='category_detail'),
    path('show_details/', show_details, name='show_details'),
    path('dj/<int:dj_id>/', dj_detail, name='dj-detail'),
    path('radio-jockey/', radio_jockey, name='radio-jockey'),
    path('faq/', faq, name='faq'),
    path('sponsor/', sponsor, name='sponsor'),
    path('contact/', contact, name='contact'),
    path('live_shows/', live_shows, name='live_shows'),
    path('previous_shows/', previous_shows, name='previous_shows'),
    path('upcoming_shows/', upcoming_shows, name='upcoming_shows'),
    path('subscribe/', subscribe, name='subscribe'),
    path('podcast_schedule/', podcast_schedule, name='podcast_schedule'),
    path('webchat/', webchat, name='webchat'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
