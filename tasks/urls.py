from django.urls import path
from .views import home, analyze_tasks

urlpatterns = [
    path('', home, name='home'),
    path('api/analyze/', analyze_tasks, name='analyze_tasks'),
]
