from django import forms
from .models import Proo


class Proo_form(forms.ModelForm):
	class Meta:
		model = Proo
		fields =[
		'name',
		'descrip'
		]
