from django import forms

class TodoInputForm(forms.Form):
    task = forms.CharField(max_length=10)
    # desc = forms.CharField(max_length=5)