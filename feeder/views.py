from django.views.generic import ListView
from feeder.models import Article

class NewsletterView(ListView):
    model = Article
    template_name = "feeder/newsletter.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["articles"] = Article.objects.filter().order_by("-pub_date")[:12]
        return context
