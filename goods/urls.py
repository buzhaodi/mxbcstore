

from django.urls import path,include
from . import views

urlpatterns = [
    path('goods', views.goods),
    path('ratings',views.ratings),


]

