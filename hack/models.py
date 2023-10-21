from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    MEAL_PLANS = [
        ('All Access', 'All Access'),
        ('15 Meal', '15 Meal'),
        # Add more options if needed
    ]
    meal_plan = models.CharField(max_length=50, choices=MEAL_PLANS)
    current_dining_dollars = models.PositiveIntegerField()
