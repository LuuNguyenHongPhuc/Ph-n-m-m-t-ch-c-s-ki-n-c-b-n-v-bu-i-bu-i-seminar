# Generated by Django 5.1.4 on 2025-01-03 12:47

import datetime
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(default='', max_length=255)),
                ('name', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='EventModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(default='')),
                ('max_people', models.IntegerField(default=0)),
                ('start_time', models.DateField(default=datetime.date.today)),
                ('end_time', models.DateField(default=datetime.date.today)),
                ('all_user_registed', models.ManyToManyField(blank=True, related_name='registered_events', to=settings.AUTH_USER_MODEL)),
                ('images', models.ManyToManyField(blank=True, related_name='events', to='event.image')),
            ],
        ),
    ]
