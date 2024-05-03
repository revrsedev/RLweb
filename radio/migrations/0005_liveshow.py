# Generated by Django 5.0.4 on 2024-05-02 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0004_alter_podcast_day_of_week'),
    ]

    operations = [
        migrations.CreateModel(
            name='LiveShow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('dj_name', models.CharField(max_length=100)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('live_status', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to='shows/player/')),
                ('audio_stream_url', models.URLField()),
            ],
        ),
    ]
