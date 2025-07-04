from django.urls import path
from . import views

urlpatterns = [
    path('', views.split_bill, name='home'),
]