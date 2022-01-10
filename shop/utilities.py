from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_email(email_from, name, subject):

    email_to = settings.DEFAULT_EMAIL_TO
    subject = 'New contact'
    text_content = 'You have a new contact'
    html_content = render_to_string('email_notify_shop.html',{'name': name, 'email_from': email_from, 'subject': subject})

    msg = EmailMultiAlternatives(subject, text_content, [email_to])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()