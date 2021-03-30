from django import forms
class customerRegistartion(forms.Form):
    name = forms.CharField()
    last = forms.CharField()
    email = forms.EmailField()



