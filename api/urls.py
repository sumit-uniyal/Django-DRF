from email_auth.views import *
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'sumit', sumit, basename='sumit')
urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
    path('index/', index, name="index"),
    path('index/', index, name="index"),
    path('mail_sea/', mail_sea, name="mail_sea"),
    path('login/', login, name="login")
]