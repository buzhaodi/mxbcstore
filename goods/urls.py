

from django.urls import path,include
from . import views

urlpatterns = [
    path('good', views.good),
    path('ratings',views.ratings),


]

