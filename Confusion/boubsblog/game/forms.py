from django import forms
from .models import SignUp

class Contact(forms.Form):
    full_name=forms.CharField()
    email=forms.CharField()
    message=forms.CharField()
    

class SignUpForm(forms.ModelForm):
    class Meta:
        model=SignUp
        fields=['full_name','email']
    def clean(self):
        email=self.cleaned_data.get('email')
        a,b=email.split("@")
        print a
        print b
        x,y=b.split('.')
        print x
        print y
        if y != "com":
            raise forms.ValidationError("Please extention is .COM")

        print email
    def clean(self):
       x=self.cleaned_data.get('full_name')
       print x
