from django import forms
from .models import User, Uploader
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username","email","password1","password2")
        widgets = {
             "username" : forms.TextInput(attrs={"class":"",}),
             "email" : forms.EmailInput(attrs={"class":"",}),
             "password1" : forms.PasswordInput(attrs={"class":"",}),
             "password2" : forms.PasswordInput(attrs={"class":"",}),
             "profile_pic" : forms.FileInput(attrs={"class":"",}),
        }

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("Username's already taken.")

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError("Email already in use")

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")

        return password2

class CreateUploaderForm(forms.ModelForm):
    class Meta():
        model = Uploader
        fields = ("reg_number","faculty","department","phone_number","profile_pic")
        widgets = {
             "reg_number" : forms.TextInput(attrs={"class":"",}),
             "faculty" : forms.Select(attrs={"class":"",}),
             "department" : forms.Select(attrs={"class":"",}),
             "phone_number" : forms.TextInput(attrs={"class":"",}),
        }
class Loginform(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)



    class Meta:
        fields = ("email","password")
        widgets = {
             "email" : forms.EmailInput(attrs={"class":"",}),
             "password" : forms.PasswordInput(attrs={"class":"",}),
        }



    def clean(self):
        email = self.cleaned_data['email']
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise forms.ValidationError("Email is not registered")

        password = self.cleaned_data["password"]
        user = authenticate(email=email, password=password)
        if user == None:
            raise forms.ValidationError("You entered an incorrect password")

        return self.cleaned_data
