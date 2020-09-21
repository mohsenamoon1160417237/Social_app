from django.contrib.auth.models import User
from django import forms
from .models import UserProfile


class UserRegistrationForm(forms.ModelForm):


	password = forms.CharField(max_length=20 , widget=forms.PasswordInput , label='Password')
	password2 = forms.CharField(max_length=20 , widget=forms.PasswordInput , label="Repeat password")


	class Meta:

		model = User
		fields = ['username' , 'email']


	def clean_password2(self):

		cd = self.cleaned_data

		if cd['password'] != cd['password2']:

			raise forms.ValidationError("Passwords must match")

		return cd['password2']

 

class UserEditProfileForm(forms.ModelForm):


	class Meta:

		model = UserProfile
		fields = ['image' , 'age']




class UserEditForm(forms.ModelForm):

	class Meta:

		model = User
		fields = ['first_name' , 'last_name']