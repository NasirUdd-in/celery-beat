# myapp/forms.py
from django import forms

class AdditionForm(forms.Form):
    number1 = forms.IntegerField(label='Number 1')
    number2 = forms.IntegerField(label='Number 2')
    delay_minutes = forms.IntegerField(label='Delay (in minutes)')


# forms.py

from django import forms

class ScheduleUpdateForm(forms.Form):
    schedule_interval = forms.IntegerField(label='Enter Schedule Interval (in seconds)')
