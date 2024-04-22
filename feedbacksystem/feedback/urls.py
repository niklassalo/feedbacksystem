from django.urls import path
from .views import submit_feedback, feedback_success, home

urlpatterns = [
    path('', home, name='home'),
    path('submit/', submit_feedback, name='submit_feedback'),
    path('success/', feedback_success, name='feedback_success'),
]