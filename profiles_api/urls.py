from django.urls import path

from profiles_api import views

urlpatterns = [
    path('hola-view/', views.HolaApiView.as_view()),
]
