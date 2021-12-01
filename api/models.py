from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from datetime import datetime    
from django.contrib.postgres.fields import ArrayField
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect

import os

class Newsletter(models.Model):
    email = models.EmailField(max_length = 64)
    date_added = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):  
        return reverse("index")

    def __str__(self):
        return self.email


class Mail(models.Model):
    sender = models.EmailField(max_length = 255) 
    subject = models.CharField(max_length = 78)
    body = models.CharField(max_length = 40000)
    recipients_list = ArrayField(models.EmailField(max_length = 255))

    def get_absolute_url(self):  
        return reverse("mail")

    def __str__(self):
        return self.subject

    class Meta:
        ordering = ['-id', ]
