from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

# Formulaire de Connexion (Patient/Docteur)
class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Nom d'utilisateur ou Email",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Entrez votre identifiant'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': '••••••••'
        })
    )

# Formulaire d'Inscription Patient (Votre version améliorée)
class PatientSignUpForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'exemple@domaine.com'
        })
    )
    phone = forms.CharField(
        max_length=15,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '+225...'
        })
    )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'phone']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_patient = True  # Définit automatiquement le rôle
        if commit:
            user.save()
        return user

# Formulaire d'Inscription Docteur (Complément)
class DoctorSignUpForm(UserCreationForm):
    license_number = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Numéro de licence médicale'
        })
    )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'license_number']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_doctor = True
        if commit:
            user.save()
        return user
