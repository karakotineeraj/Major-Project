from django import forms
from . import models


class UserCreateFrom(forms.ModelForm):
	class Meta:
		model = models.Members
		exclude = ('date_added', 'exit_allow', 'car_number', )