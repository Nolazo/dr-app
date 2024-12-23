from django import forms
from .models import Doctor

class DoctorForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    qualification = forms.CharField(max_length=100)
    contact_number = forms.CharField(max_length=15)
    email = forms.EmailField()
    address = forms.CharField(widget=forms.Textarea)
    biography = forms.CharField(widget=forms.Textarea)
    is_on_vacation = forms.BooleanField(initial=False, required=False)

    def save(self):
        data = self.cleaned_data
        doctor = Doctor.objects.create(
            first_name=data['first_name'],
            last_name=data['last_name'],
            qualification=data['qualification'],
            contact_number=data['contact_number'],
            email=data['email'],
            address=data['address'],
            biography=data['biography'],
            is_on_vacation=data['is_on_vacation']
        )
        return doctor 