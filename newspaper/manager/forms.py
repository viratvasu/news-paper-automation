from django import forms
from .models import Manager

class ManagerForm(forms.ModelForm):
	class Meta:
		model=Manager
		fields=['manager_name',]

		widgets={
			'manager_name':forms.TextInput(attrs={'placeholder':'Branch Manager Name'}),
		}
