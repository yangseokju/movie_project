from datetime import datetime
from django import forms
from .models import Movie
# from django.forms.widgets import NumberInput
class MovieForm(forms.ModelForm):

    # title = forms.TextInput()
    genre = forms.ChoiceField(choices=[('코미디', '코미디'), ('공포', '공포'), ('로맨스', '로맨스'),('드라마', '드라마'),('멜로', '멜로')], required=True)
    score = forms.FloatField(
        widget=forms.TextInput(attrs={
            'step': 0.5,
            'min': 0,
            'max': 5,
        })
        )
    # release_date = forms.DateTimeField(widget=NumberInput(attrs={'type': 'date'}), label="Release Date")
    release_date = forms.DateField(
        widget=forms.DateInput(
            attrs={'type': 'date', 'class': 'form-control'}
            )
        )
    class Meta:
        model = Movie
        fields = '__all__'