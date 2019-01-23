from .models import Person
from django.forms import ModelForm

class PersonForm(ModelForm):
    class Meta:
        model  = Person
        fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']