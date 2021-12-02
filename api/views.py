from django.shortcuts import render
from .models import Mail, Newsletter
from .forms import MailForm, NewsletterSignupForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .models import Newsletter, Mail
from django.core.mail import send_mass_mail
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib, ssl
from django.template.loader import render_to_string
from django import template
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from feeder.models import Article
from django.core.mail import EmailMultiAlternatives


class NewsletterSignUpView(CreateView):
    model = Newsletter
    form_class = NewsletterSignupForm
    template_name = 'api/signup.html'

    def form_valid(self, form):
        return super(NewsletterSignUpView, self).form_valid(form)

class AddEMailView(LoginRequiredMixin, CreateView):
    model = Mail
    form_class = MailForm
    template_name = 'api/send.html'
    
    def form_valid(self, form):
        super(AddEMailView, self).form_valid(form)
        
        form.instance.sender = self.request.user.email
        
        port = 465
        sender_email = self.request.user.email
        reciever_email = list(Newsletter.objects.values_list('email', flat=True))
        reciever_email += form.instance.recipients_list
        password = self.request.user.gapps_key
        subject = form.instance.subject

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = ', '.join(reciever_email)
        message["Subject"] = subject

        html_template='feeder/newsletter.html'
        context = {'articles': Article.objects.filter().order_by("-pub_date")[:12]}
        msg_html = render_to_string(html_template, context)
        message.attach(MIMEText(msg_html, "html"))
        #message.attach_alternative(html_content, "text/html")
        message=message.as_string()


        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, reciever_email, message)

        return super(AddEMailView, self).form_valid(form)
