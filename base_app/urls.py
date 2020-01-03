from django.urls import path

from . import views
from django.conf.urls import url

app_name = 'base_app'

urlpatterns = [
    path('', views.homeview, name='home_page'),
]
