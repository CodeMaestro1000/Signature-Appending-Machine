from django import forms
from django.forms import widgets
from .models import Request, Signatory

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        full_name = forms.CharField(required=True)
        school_id = forms.CharField(required=True)
        email = forms.EmailField(required=True)
        signatory = forms.ChoiceField(required=True)
        purpose = forms.CharField(required=True)
        fields = ['full_name', 'school_id', 'email', 'signatory', 'purpose']

        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': "form-control request-input",
                'placeholder': "FIRST NAME",
                'id': "request-full-name",
            }),
            'school_id': forms.TextInput(attrs={
                'class': "form-control request-input",
                'id': "requester-id",
                'placeholder': "SCHOOL ID",
            }),
            'email': forms.TextInput(attrs={
                'class': "form-control request-input",
                'placeholder': "name@example.com",
                'id': "request-email",
            }),
            'signatory': forms.Select(attrs={
                'class': "form-control request-input",
                'id': "signatory",
            }),
            'purpose': forms.Textarea(attrs={
                'class': "form-control request-input",
                'placeholder' : "Maximum of 300 characters",
                'id' : "request-purpose",
                'style' : "height: 100px",
                'maxlength' : "300"
            }),
        }