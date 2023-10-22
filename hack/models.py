from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    MEAL_PLANS = [
        ('All Access + $50 Dining Dollars', 'All Access + $50 Dining Dollars'),
        ('15 Meal + $160 Dining Dollars', '15 Meal + $160 Dining Dollars'),
        ('12 Meal + $210 Dining Dollars', '12 Meal + $210 Dining Dollars'),
        ('10 Meal + $400 Dining Dollars', '10 Meal + $400 Dining Dollars'),
        # Add more options if needed
    ]

    meal_plan = models.CharField(max_length=100, choices=MEAL_PLANS)
    current_dining_dollars = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f"{self.user.username}'s Profile"
