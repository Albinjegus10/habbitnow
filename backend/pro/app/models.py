from django.db import models

class UserSettings(models.Model):
    notifications = models.BooleanField(default=True)
    dark_mode = models.BooleanField(default=False)
    reminder_time = models.TimeField(default="09:00")
    weekend_reminders = models.BooleanField(default=True)
    sound_enabled = models.BooleanField(default=True)
    vibration_enabled = models.BooleanField(default=True)
    data_backup = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Settings"

class Habit(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class HabitTracker(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name='trackers')
    date = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.habit.name} - {self.date}"
