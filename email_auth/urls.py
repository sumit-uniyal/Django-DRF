from django.urls import path
from . import views
from . import ajax
urlpatterns = [
    path('', views.home, name="home"),
    path('get_data/', ajax.get_data, name="get_data"),
    path('delete_data/', ajax.delete_data, name="delete_data"),
    path('list/', views.list, name="list"),
    path('update_email/', views.update_email, name="update_email"),

]