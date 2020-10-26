from django import forms
from .models import UserProfile
class UserProfileForm(forms.ModelForm):
	class Meta:
		model=UserProfile
		fields='__all__'
		exclude=['user','paper_boy']
 
		widgets={
			'name':forms.TextInput(attrs={'placeholder':'Your Name'}),
			'pno':forms.TextInput(attrs={'placeholder':'Contact Number'}),
			'door_num':forms.TextInput(attrs={'placeholder':'Door Number'}),
			'village':forms.TextInput(attrs={'placeholder':'Village'}),
			'mandal':forms.TextInput(attrs={'placeholder':'Mandal'}),
			'pincode':forms.NumberInput(attrs={'placeholder':'Pincode'}),
		}