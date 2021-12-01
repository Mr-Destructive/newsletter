from django.db import models
from django.shortcuts import render

class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField()
    link = models.URLField()
    image = models.URLField()
    publication_name= models.CharField(max_length=100)
    puid = models.CharField(max_length=10000)

    def __str__(self) -> str:
        return f"{self.title}"
