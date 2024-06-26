from email_auth.views import *
from django.urls import path

urlpatterns = [
    path('index/', index, name="index"),
    path('mail_sea/', mail_sea, name="mail_sea"),
    path('login/', login, name="login")
]