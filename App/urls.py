from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('',views.index),
    path('sample/',views.sample,name='sample'),
    path('sample/details/<int:id>',views.details,name='details'),
]