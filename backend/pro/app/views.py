from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny  # Since there's no user dependency
from rest_framework import status
from .models import UserSettings
from .serializer import UserSettingsSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserSettings
from .serializer import UserSettingsSerializer
from rest_framework.permissions import AllowAny

class UserSettingsView(APIView):
    permission_classes = [AllowAny]  # No authentication required

    def get(self, request):
        settings = UserSettings.objects.first()  # Fetch the first settings entry
        if settings is None:
            # Return default settings if none exist
            default_settings = {
                "notifications": True,
                "dark_mode": False,
                "reminder_time": "09:00",
                "weekend_reminders": True,
                "sound_enabled": True,
                "vibration_enabled": True,
                "data_backup": False
            }
            return Response(default_settings, status=status.HTTP_200_OK)

        serializer = UserSettingsSerializer(settings)
        return Response(serializer.data)

    def post(self, request):
        # Create default settings if none exist
        if not UserSettings.objects.exists():
            new_settings = UserSettings.objects.create(
                notifications=True,
                dark_mode=False,
                reminder_time="09:00",
                weekend_reminders=True,
                sound_enabled=True,
                vibration_enabled=True,
                data_backup=False
            )
            serializer = UserSettingsSerializer(new_settings)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response({"detail": "Settings already exist."}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        settings = UserSettings.objects.first()  # Fetch the first settings entry
        if settings is None:
            return Response({"detail": "Settings not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSettingsSerializer(settings, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



from rest_framework import generics
from .models import Habit
from .serializer import HabitSerializer
from rest_framework.permissions import AllowAny  # No user dependency anymore

class HabitListCreateView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]  # No authentication needed

    serializer_class = HabitSerializer

    def get_queryset(self):
        # Return all habits, no user dependency
        return Habit.objects.all()

    def perform_create(self, serializer):
        # Since there's no user, we don't need to save user-specific data
        serializer.save()


class HabitDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]  # No authentication needed

    serializer_class = HabitSerializer

    def get_queryset(self):
        # Return all habits, no user dependency
        return Habit.objects.all()


from rest_framework import generics
from .models import HabitTracker
from .serializer import HabitTrackerSerializer
from rest_framework.permissions import AllowAny  # No authentication needed

class HabitTrackerListCreateView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]  # No authentication needed
    serializer_class = HabitTrackerSerializer

    def get_queryset(self):
        # Return all habit trackers, no user dependency
        return HabitTracker.objects.all()

    def perform_create(self, serializer):
        habit = serializer.validated_data['habit']
        # Since there's no user, the habit does not need a user check
        serializer.save()


from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Habit, HabitTracker
import datetime

class DashboardView(APIView):
    permission_classes = [AllowAny]  # No authentication needed

    def get(self, request):
        total_habits = Habit.objects.count()  # Total habits, no user dependency
        completed_today = HabitTracker.objects.filter(
            date=datetime.date.today(), completed=True
        ).count()
        
        data = {
            'total_habits': total_habits,
            'completed_today': completed_today,
        }
        return Response(data)
