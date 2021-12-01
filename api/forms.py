from django import forms
from .models import Mail, Newsletter

class MailForm(forms.ModelForm):
    class Meta:
        model = Mail
        exclude = ['sender',]

        widgets = {
                'subject': forms.TextInput(attrs={
                    'class': 'form-control',
                    'max-length': '70',
                    }),
                'body': forms.Textarea(attrs={
                    'class': 'form-control',
                    'max-length': '40000',
                    }),
                'recipients_list': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Comma Seperated email-ids',
                    }),

                'attachment_file': forms.FileInput(attrs={
                    'class': 'form-control',}),

                }

class NewsletterSignupForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']
        
        widgets = {
                'email': forms.EmailInput(attrs={
                    'class': 'form-control',
                    'max-length':'64',
                    }),
                }
