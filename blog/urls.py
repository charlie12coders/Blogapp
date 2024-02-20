
from . import views
from django.urls import path ,include

urlpatterns = [
    path('',views.signin),
    path('register/',views.register),
    path('home/',views.home),
    path('new/',views.newPost),
    path('myPost/',views.myPost),
    path('signout/',views.signout)
]
