from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('submit', views.submit),
    path('success', views.success),
]
