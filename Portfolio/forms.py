from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter your name',
                'class': 'form-control',
                'style': 'width:100%'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter your email',
                'class': 'form-control',
                'style': 'width:100%'
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Enter your phone number',
                'class': 'form-control',
                'style': 'width:100%'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Enter your message (at least 100 characters)',
                'class': 'form-control',
                'style': 'width:100%',
                'rows': 5
            }),
        }

    def clean_message(self):
        message = self.cleaned_data.get("message")
        if len(message) < 100:
            raise forms.ValidationError("Message must be at least 100 characters long.")
        return message
