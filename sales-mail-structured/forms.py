from django import forms

class MyForm(forms.Form):
  in_area = forms.CharField(max_length=100)