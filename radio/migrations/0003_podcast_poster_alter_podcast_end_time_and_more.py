# Generated by Django 5.0.4 on 2024-05-02 15:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0002_remove_podcast_date_remove_podcast_description_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='podcast',
            name='poster',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='podcasts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='end_time',
            field=models.TimeField(default='13:00'),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='start_time',
            field=models.TimeField(default='12:00'),
        ),
    ]
