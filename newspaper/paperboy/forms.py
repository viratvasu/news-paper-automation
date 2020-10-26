from django import forms
from .models import PaperBoy

class PaperBoyForm(forms.ModelForm):
	class Meta:
		model=PaperBoy
		fields=['name','pno','pincode']

		widgets={
			'name':forms.TextInput(attrs={'placeholder':'Paper Boy Name'}),
			'pno':forms.TextInput(attrs={'placeholder':'Paper Boy Contact Number'}),
			'pincode':forms.NumberInput(attrs={'placeholder':'Paper Boy Contact Number'}),
		}