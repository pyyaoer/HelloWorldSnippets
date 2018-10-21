from django.urls import path

from . import views

urlpatterns = [
    path('', views.ajax_test, name='ajax_test'),
    path('ajax_test', views.ajax_test, name='ajax_test'),
]