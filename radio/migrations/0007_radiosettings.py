# Generated by Django 5.0.4 on 2024-05-02 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0006_alter_liveshow_image_alter_liveshow_live_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='RadioSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stream_url', models.URLField(default='https://ritmolatinoscs.radioca.st/stream?type=http&amp;nocache=7469', editable=False)),
            ],
            options={
                'verbose_name_plural': 'Radio Settings',
            },
        ),
    ]
