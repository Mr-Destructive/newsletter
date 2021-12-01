from django.urls import path
from django.views.generic import TemplateView
from .views import AddEMailView

urlpatterns = [
    path('', TemplateView.as_view(template_name='base.html'),name='index'),
    path('mail/', AddEMailView.as_view(), name='mail'),
] 
