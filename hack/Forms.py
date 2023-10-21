from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'meal_plan', 'current_dining_dollars']
        
class SelectionForm(forms.Form):
    options = [
        ('option1', 'Option 1'),
        ('option2', 'Option 2'),
        ('option3', 'Option 3'),
    ]
    
    selected_option = forms.ChoiceField(
        choices=options,
        widget=forms.RadioSelect,
    )
