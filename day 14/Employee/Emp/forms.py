from Emp.models import UsrRg
from django import forms

class UsregForm(forms.ModelForm):
	class Meta:
		model=UsrRg
		fields = ['username','email','age']
		widgets = {
		"username":forms.TextInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Username",
			"required":True,
			}),
		 	"email":forms.EmailInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Email id",
			"required":True,
			}),
		"age":forms.NumberInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter age",
			"required":True,
			}),

		}
class Userupdate(forms.ModelForm):
	class Meta:
		model=UsrRg
		fields = ['username','email','age']
		widgets = {
		"username":forms.TextInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Username",
			"required":True,
			}),
		"email":forms.EmailInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Email id",
			"required":True,
			}),
		"age":forms.NumberInput(attrs = {
			"class":"form-control",
			"placeholder":"update age",
			"required":True,
			}),

		}