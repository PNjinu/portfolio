from django import forms
from django.forms import ModelForm, TextInput, EmailInput, Textarea
from .models import ContactMessages

class ContactForm(ModelForm):
    #name = forms.CharField(required=True)
    #email =forms.EmailField(required=True)
    #subject = forms.CharField(required=True)
    #message = forms.Textarea(required=True)

    class Meta:
        model = ContactMessages
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': TextInput(attrs={
                'placeholder': 'name',
            }),
            'email': EmailInput(attrs={
                'placeholder': "email",
            }),
            'subject': TextInput(attrs={
                'placeholder' : "subject",
                'class' : "box",
            }),
            'message': Textarea(attrs={
                'placeholder' : "message", 
                'cols': "30", 
                'rows':"10",
            }),
        }