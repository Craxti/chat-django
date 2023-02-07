from django.db import models
from django.conf import settings


# Create your models here.


class ChatData(models.Model):
    person_head = models.CharField(max_length=50)
    person_tail = models.CharField(max_length=50)
    body = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now_add=True)

class ChatRelation(models.Model):
    person_head = models.CharField(max_length=50)
    person_tail = models.CharField(max_length=50)
    unread_msg_present = models.IntegerField(default=0)
    unread_msg_previous = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=True)