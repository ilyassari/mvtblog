from django import forms
from django.core.mail import send_mail

from common.settings import EMAIL_HOST_USER

class ContactForm(forms.Form):
    """docstring for Contact Form."""
    title = forms.CharField(label="Konu", max_length=30)
    email = forms.EmailField(label="E-posta",required=True, max_length=60)
    full_name = forms.CharField(label="İsim Soyisim",max_length=30, strip=True)
    message = forms.CharField(label="Mesajınız", widget=forms.Textarea())

    def send_email(self, title, sender, message):
        send_mail(
            subject=f'Yeni İletişim Mesajı: {title} from {sender}',
            message=message,
            from_email=EMAIL_HOST_USER,
            recipient_list=[EMAIL_HOST_USER],
            fail_silently=False
        )
