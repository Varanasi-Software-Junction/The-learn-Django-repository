from django import forms


class StudentForm(forms.Form):
    name = forms.CharField(max_length=200)
    rollno = forms.IntegerField()
