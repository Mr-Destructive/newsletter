from django.urls import path
from django.views.generic import TemplateView
from .views import AddEMailView, NewsletterSignUpView
from feeder.views import NewsletterView

urlpatterns = [
    #path('', TemplateView.as_view(template_name='base.html'),name='index'),
    path('', NewsletterView.as_view(), name='index'),
    path('mail/', AddEMailView.as_view(), name='mail'),
    path('newsletter/', NewsletterSignUpView.as_view(), name="signup"),
] 
