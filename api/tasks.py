from celery import shared_task
from django.core.mail import send_mail
from .services import save_visit
from plantext.celery import app

@shared_task
def stats():
    send_mail(
        "We have new users!",
        "We have a new book: ",
        "plantext@bookshop.ru",
        ["examplemail@mail.com"],
        fail_silently=False,
    )

@shared_task
def visits():
    save_visit()