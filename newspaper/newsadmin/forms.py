from django import forms
from . models import Branch,NewsPaper,Magazine

class BranchForm(forms.ModelForm):
	class Meta:
		model=Branch
		fields="__all__"
		widgets={
			'name':forms.TextInput(attrs={'placeholder':'Branch Name'}),
			'pno':forms.TextInput(attrs={'placeholder':'Contact Number'}),
			'address':forms.TextInput(attrs={'placeholder':'Adress or Landmark'}),
		}
class NewsPaperForm(forms.ModelForm):
	class Meta:
		model=NewsPaper
		fields="__all__"
		widgets={
			'name':forms.TextInput(attrs={'placeholder':'News Paper Name'}),
			'image':forms.FileInput(attrs={'class':'form-control-file'}),
			'language':forms.TextInput(attrs={'placeholder':'Language'}),
			'price':forms.NumberInput(attrs={'placeholder':'Price'}),
		}
class MagazineForm(forms.ModelForm):
	class Meta:
		model=Magazine
		fields="__all__"
		widgets={
			'name':forms.TextInput(attrs={'placeholder':'Magazine Name'}),
			'image':forms.FileInput(attrs={'class':'form-control-file'}),
			'language':forms.TextInput(attrs={'placeholder':'Language'}),
			# 'magazine_type':forms.ChoiceField(),
			'price':forms.NumberInput(attrs={'placeholder':'Price'}),
		}	
