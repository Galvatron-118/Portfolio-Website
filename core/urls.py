from django.urls import path
from .views import HomeTemplateView
from .import views

urlpatterns = [
    path('',HomeTemplateView.as_view()),
    
]