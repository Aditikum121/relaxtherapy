from django import forms


class usersform(forms.Form):
    num1=forms.CharField(label='value1', widget=forms.Textarea(attrs={'class':"form-control"} ))
    num2=forms.CharField()
    email1= forms.EmailField()
    

