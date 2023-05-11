from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from django.forms import ModelForm, TextInput
from .models import Estimation

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

	def __init__(self, *args, **kwargs):
		super(NewUserForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_show_labels = False
		# self.fields['username'].label = "False"
		# # self.helper.help_text = "False"
		self.fields['username'].help_text = ""
		self.fields['password1'].help_text = ""
		self.fields['password2'].help_text = ""

class EstimationForm(ModelForm):

	class Meta:
		model = Estimation
		fields = ["projectname"]
		widgets = {
			"projectname": TextInput(attrs = {
			"class": "form-style",
			"placeholder": "Название проекта"
			})
		}