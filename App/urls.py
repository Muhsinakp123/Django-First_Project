from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('',views.index),
    path('sample/',views.sample,name='sample'),
    path('sample/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
    path('sample/add/', views.add, name='add'),
    path('sample/add/addmember/', views.addmember, name='addmember'),
    path('sample/delete_member/<int:id>', views.delete_member, name='delete_member'),
    path("sample/update/<int:id>/", views.update, name="update"),
    path("sample/update_member/<int:id>/", views.update_member, name="update_member"),
   

]