from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "form-control",
            'placeholder': 'John Doe'
        }
    ))
    email = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "form-control",
            'placeholder': 'your@email.com'
        }
    ))
    address = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "form-control",
            'placeholder': '1234 address st.(optional)'
        }
    ))
    message = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "form-control",
            'placeholder': 'message'
        }
    ))
    phone = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "form-control",
            'placeholder': '555-555-5555'
        }
    ))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['address'].required = False

    class Meta:
        model = Contact
        fields = '__all__'