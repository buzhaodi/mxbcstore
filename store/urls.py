

from django.urls import path,include
from . import views

urlpatterns = [
    path('seller', views.seller),


]

