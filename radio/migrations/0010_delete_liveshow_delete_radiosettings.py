# Generated by Django 5.0.4 on 2024-05-02 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0009_radiosettings_stream_url'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LiveShow',
        ),
        migrations.DeleteModel(
            name='RadioSettings',
        ),
    ]
