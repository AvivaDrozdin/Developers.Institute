from django import forms
from .models import Film, Director

#create forms to add films & director

class AddFilmForm(forms.ModelForm):
    class Meta:
        model= Film
        fields = '__all__'

class AddDirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = '__all__'
        labels = {
        'fname': 'First Name',
        'lname': 'Last Name'
    }

        