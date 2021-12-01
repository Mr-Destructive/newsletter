from django.shortcuts import render
from .models import Mail, Newsletter
from .forms import MailForm, NewsletterSignupForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .models import Newsletter

class AddEMailView(LoginRequiredMixin, CreateView):
    model = Mail
    form_class = MailForm
    template_name = 'api/send.html'
    
    def form_valid(self, form):
        super(AddEMailView, self).form_valid(form)
        
        form.instance.sender = self.request.user.email
        
        port = 465
        sender_email = self.request.user.email
        reciever_email = form.instance.recipients_list
        password = self.request.user.gapps_key
        body = form.instance.body
        subject = form.instance.subject

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = ','.join(reciever_email)
        message["Subject"] = subject
        
        message.attach(MIMEText(body, "plain"))
        
        message = message.as_string()

        
        sendmails(sender_email, reciever_email, password, message, send_time)

        return super(AddMailView, self).form_valid(form)
