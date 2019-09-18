from django.urls import path, include
from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
router.register('hola-viewset', views.HolaViewSet, base_name='hola-viewset')
router.register('profile', views.UserProfileViewSet) #Aca no ponemos base_name por que DRF lo deduce

urlpatterns = [
    path('hola-view/', views.HolaApiView.as_view()),
    path('', include(router.urls)),
]
