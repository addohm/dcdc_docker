from django import forms
from django.core.mail import send_mail
from django.core.validators import EmailValidator
from django.db import transaction
from decouple import config
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'phone', 'subject', 'message')
        exclude = ('when_sent', 'replied', 'when_replied')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def save(self):
        instance = super(ContactForm, self).save()
        print(instance.subject)

        @transaction.on_commit
        def contact_sendemail():
            send_mail(
                instance.subject,
                instance.message,
                config("EMAIL_HOST_USER"),
                [instance.email],
                fail_silently=False,
            )
            print("Email sent, maybe?")
        print("Form saved, check email.")
        return instance