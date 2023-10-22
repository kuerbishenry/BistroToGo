from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'meal_plan', 'current_dining_dollars']
        
class SelectionForm(forms.Form):
    options = [
        ('Swap', 'Swap'),
        ('Buy', 'Buy'),
    ]
    
    selected_option = forms.ChoiceField(
        choices=options,
        widget=forms.RadioSelect,
    )
