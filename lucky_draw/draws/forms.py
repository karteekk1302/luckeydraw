from django import forms
from datetime import datetime

class GenerateDrawResultsForm(forms.Form):
    # Set the default value for the date field to today's date
    date = forms.DateField(initial=datetime.today().date, widget=forms.SelectDateWidget())
    
    # Set the default value for the time field to the current time
    time = forms.TimeField(initial=datetime.now().time().strftime('%H:%M'), widget=forms.TimeInput(format='%H:%M'))
