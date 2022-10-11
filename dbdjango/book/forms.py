from django import forms
from django.forms import ModelForm

from .models import BooksModel


class BookForm(ModelForm):
    class Meta:
        model = BooksModel
        fields = fields = '__all__'


class StudentForm(forms.Form):
    name = forms.CharField(max_length=200)
    rollno = forms.IntegerField()
