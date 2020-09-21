from django import forms
from .models import Image



class ImagePostForm(forms.ModelForm):


	class Meta:

		model = Image
		fields = ['photo' , 'title' , 'description']


