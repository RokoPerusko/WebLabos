from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username

class Calendar(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    calendar = models.ForeignKey(Calendar, related_name='events', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_all_day = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    assigned_users = models.ManyToManyField(User, related_name='tasks')

    def __str__(self):
        return self.title

class Diary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    entry_date = models.DateField()
    content = models.TextField()

    def __str__(self):
        return f"Diary of {self.user.username} - {self.entry_date}"

