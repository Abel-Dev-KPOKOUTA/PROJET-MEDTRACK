from django import forms
from .models import PatientProfile

class PatientProfileForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False,
        label="Date de naissance"
    )

    class Meta:
        model = PatientProfile
        fields = ['phone', 'gender', 'date_of_birth', 'address', 'medical_history']
        labels = {
            'phone': 'Téléphone',
            'gender': 'Genre',
            'address': 'Adresse postale',
            'medical_history': 'Antécédents médicaux',
        }
        widgets = {
            'medical_history': forms.Textarea(attrs={'rows': 4}),
            'address': forms.Textarea(attrs={'rows': 3}),
        }