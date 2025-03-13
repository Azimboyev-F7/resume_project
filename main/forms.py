from django import forms
from .models import Recieve


class RecieveForm(forms.ModelForm):
    class Meta:
        model = Recieve
        fields = ['first_name', 'last_name', 'email', 'message']

    def __init__(self, *args, **kwargs):
        super(RecieveForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['class'] = 'form-control'

