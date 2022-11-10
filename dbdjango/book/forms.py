from django import forms
from django.forms import ModelForm, TextInput

from .models import BooksModel


class BookForm(ModelForm):
    class Meta:
        model = BooksModel
        # fields = fields = '__all__'
        fields = ['bookname', 'subject', 'price']
        widgets = {
            'bookname': TextInput(attrs={
                'class': "form-control",

                'placeholder': 'Book Name'
            })}


class StudentForm(forms.Form):
    name = forms.CharField(max_length=200)
    rollno = forms.IntegerField()
    # last_modified = models.DateTimeField(auto_now_add = True)
    # img = models.ImageField(upload_to = "images/"
