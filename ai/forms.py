from django import forms
from . import models


class UserCreateFrom(forms.ModelForm):
    class Meta:
        model = models.Members
        exclude = ('date_added', 'exit_allow', 'car_number', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['owner'].widget.attrs.update({'placeholder': 'John Doe'})
        self.fields['flat_address'].widget.attrs.update({'placeholder': 'D-303, Imagine Land'})
        self.fields['phone_number'].widget.attrs.update({'placeholder': '2345****90'})
        self.fields['email_id'].widget.attrs.update({'placeholder': 'abc@xyz.com'})
