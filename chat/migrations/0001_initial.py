# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('handle', models.TextField()),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now, db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('label', models.SlugField(serialize=False, primary_key=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='room',
            field=models.ForeignKey(related_name='messages', to='chat.Room'),
        ),
    ]
