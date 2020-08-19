from django.contrib import admin
from django.urls import path,include
from first_contact import views as v

urlpatterns = [
    path('home',v.home),
    path('',v.home_contact),
    path('insertContact',v.insertContact),
    path('ViewContact',v.ViewContact),
    path('delete/<int:id>',v.delete),
    path('update/<int:id>',v.update),
    path('addUser/',v.addUser),
    path('userList/',v.userList),
    path('contactByUser/',v.contactByUser),
    path('signIn/',v.signIn),
    path('signout',v.signout),
   
]