from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Room(models.Model):
    user = models.ForeignKey(User)
    label = models.SlugField(primary_key=True)

    def __unicode__(self):
        return self.label


class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages')
    handle = models.TextField()
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)

    def __unicode__(self):
        return '[{timestamp}] {handle}: {message}'.format(**self.as_dict())
    
    def as_dict(self):
        return {'handle': self.handle, 'message': self.message}
