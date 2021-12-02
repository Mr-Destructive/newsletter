from django.core.management.base import BaseCommand

import feedparser
from dateutil import parser

from feeder.models import Article

def save_new_article(feed):
        article_title = feed.channel.title

        for item in feed.entries:
            if not Article.objects.filter(puid=item.guid).exists():
                article = Article(
                    title=item.title,
                    description=item.description,
                    pub_date=parser.parse(item.published),
                    link=item.link,
                    publication_name=article_title,
                    puid=item.guid,
                )
                article.save()

def geeksforgeeks():
    _feed = feedparser.parse("https://www.cdn.geeksforgeeks.org/feed/")
    save_new_article(_feed)

def devto():
    _feed = feedparser.parse("https://dev.to/feed/")
    save_new_article(_feed)

def tech_republic():
    _feed = feedparser.parse("https://www.techrepublic.com/rssfeeds/articles/")
    save_new_article(_feed)

def freecodecamp():
    _feed = feedparser.parse("https://medium.com/feed/free-code-camp")
    save_new_article(_feed)

def medium():
    _feed = feedparser.parse("https://medium.com/feed/better-programming")
    save_new_article(_feed)

def hackernoon():
    _feed = feedparser.parse("https://cdn.hackernoon.com/feed")
    save_new_article(_feed)

class Command(BaseCommand):
    def handle(self, *args, **options):
        geeksforgeeks()
        devto()
        tech_republic()
        freecodecamp()
        medium()
        hackernoon()
