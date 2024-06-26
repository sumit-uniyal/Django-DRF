from django.core.mail import send_mail
from django.conf import settings
 
def send_emails(subject, message, email):

    subjects = subject
    messages = message
    from_email = settings.EMAIL_HOST_USER
    if not isinstance(email, list):
        to_email = [email]
    else:
        to_email = email
    send_mail(subjects, messages, from_email, to_email)