from . import views
from django.urls import path

app_name = 'readcsv'

urlpatterns = [
    path("", views.index, name='index'),
]