from django import forms

class TodoInputForm(forms.Form):
    task = forms.CharField(max_length=10)