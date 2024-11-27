from django.urls import path
from .views import (
    UserSettingsView, HabitListCreateView, HabitDetailView,
    HabitTrackerListCreateView, DashboardView
)

urlpatterns = [
    path('settings/', UserSettingsView.as_view(), name='user-settings'),
    path('habits/', HabitListCreateView.as_view(), name='habit-list-create'),
    path('habits/<int:pk>/', HabitDetailView.as_view(), name='habit-detail'),
    path('habit-tracker/', HabitTrackerListCreateView.as_view(), name='habit-tracker'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
