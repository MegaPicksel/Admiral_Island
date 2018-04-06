from __future__ import absolute_import
from celery import Celery
from django.core.mail import send_mail
from django.template import loader

app = Celery('tasks', broker='amqp://guest:guest@localhost:5672/')

@app.task
def contact_email(name, message, email, contact):
    # Email has an email template that data is passed into
    # Note, this function needs four parameters, the values of which come from views.py.
    # Context of email here

    ctx = {
        'name': name,
        'message': message,
        'email': email,
        'contact': contact,
    }

    # Load data into template.

    content = loader.get_template('info/contact_email.txt').render(ctx)

    # Subject of email

    subject = 'Admiral Island and Port Owen'

    # Send the email
    send_mail(
        subject,
        content,
        email,
        ['stuartsargent208@gmail.com'],
        fail_silently=False,
    )

