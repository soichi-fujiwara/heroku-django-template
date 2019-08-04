from django import forms

class MyForm(forms.Form):
  #ラベル名
  inArea = forms.CharField(max_length=100)