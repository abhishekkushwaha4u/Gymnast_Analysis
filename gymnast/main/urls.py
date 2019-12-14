from django.urls import path

from . import views

urlpatterns = [
    path('', views.SampleEndPoint.as_view()),
    path('check/', views.SampleRun.as_view()),
]