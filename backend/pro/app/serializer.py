from rest_framework import serializers
from .models import UserSettings

class UserSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSettings
        fields = ['id', 'notifications', 'dark_mode', 'reminder_time', 'weekend_reminders', 'sound_enabled', 'vibration_enabled', 'data_backup', 'created_at', 'updated_at']

from rest_framework import serializers
from .models import Habit

class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ['id', 'name', 'description', 'created_at', 'updated_at']


from rest_framework import serializers
from .models import HabitTracker

class HabitTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitTracker
        fields = ['id', 'habit', 'date', 'completed']
