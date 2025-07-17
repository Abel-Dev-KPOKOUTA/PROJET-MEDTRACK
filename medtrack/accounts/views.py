from django.shortcuts import render, redirect
from patients.models import PatientProfile
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.urls import reverse_lazy , reverse
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import DoctorSignUpForm, PatientSignUpForm, CustomLoginForm
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

User = get_user_model()

# --- Vue inscription patient avec formulaire HTML custom ---
def custom_patient_signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        date_of_birth = request.POST.get('date_of_birth', None)
        gender = request.POST.get('gender', '')
        address = request.POST.get('address', '')
        medical_history = request.POST.get('medical_history', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')

        # Validation simple
        if not all([first_name, last_name, username, email, phone, password1, password2]):
            messages.error(request, "Tous les champs obligatoires doivent être remplis.")
            return render(request, 'accounts/signup_patient.html')

        if password1 != password2:
            messages.error(request, "Les mots de passe ne correspondent pas.")
            return render(request, 'accounts/signup_patient.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Ce nom d'utilisateur existe déjà.")
            return render(request, 'accounts/signup_patient.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Cet email existe déjà.")
            return render(request, 'accounts/signup_patient.html')

        # Création de l'utilisateur
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1,
            first_name=first_name,
            last_name=last_name,
            is_patient=True,
            is_active=True
        )

        # Création du profil patient
        PatientProfile.objects.create(
            user=user,
            phone=phone,
            gender=gender,
            date_of_birth=date_of_birth if date_of_birth else None,
            address=address,
            medical_history=medical_history
        )

        messages.success(request, "Votre compte patient a été créé avec succès ! Vous pouvez maintenant vous connecter.")
        return redirect('accounts:login_user')

    return render(request, 'accounts/signup_patient.html')

# --- Vue inscription médecin (formulaire Django) ---
class DoctorSignUpView(CreateView):
    model = User
    form_class = DoctorSignUpForm
    template_name = 'accounts/signup_doctor.html'
    success_url = reverse_lazy('accounts:login_user')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.instance
        user.is_doctor = True
        user.is_active = False  # Désactivé jusqu'à validation admin
        user.save()
        messages.success(
            self.request,
            "Votre demande d'inscription médecin a été envoyée. "
            "Vous recevrez un email après validation par l'administrateur."
        )
        return response

# --- Vue inscription patient (formulaire Django, non utilisée si custom_patient_signup est utilisée) ---
class PatientSignUpView(CreateView):
    model = User
    form_class = PatientSignUpForm
    template_name = 'accounts/signup_patient.html'
    success_url = reverse_lazy('accounts:login_user')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.instance
        user.is_patient = True
        user.is_active = True  # Activé immédiatement
        user.save()
        if hasattr(form, 'save_profile'):
            form.save_profile(user)
        messages.success(
            self.request,
            "Votre compte patient a été créé avec succès ! "
            "Vous pouvez maintenant vous connecter."
        )
        return response

# --- Connexion ---
class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'accounts/login.html'

    def get_success_url(self):
        # Redirige vers le dashboard patient après connexion
        return reverse_lazy('patients:dashboard')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request, 
            f"Connexion réussie. Bienvenue {form.get_user().username}  sur MedTrack!"
        )
        return response

    def form_invalid(self, form):
        messages.error(
            self.request,
            "Identifiants incorrects. Veuillez réessayer."
        )
        return super().form_invalid(form)

# --- Déconnexion ---
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('accounts:accueil')

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        # Ajoute le message après la déconnexion et la redirection
        messages.info(request, "Vous avez été déconnecté avec succès.")
        return HttpResponseRedirect(self.next_page)
    
# --- Accueil ---
def accueil_page(request):
    return render(request, 'accounts/accueil.html')

def patient_signup(request):
    # ... création de l'utilisateur ...
    messages.success(request, "Inscription terminée ! Connectez-vous.")
    return redirect('accounts:login_user')

def demonstration(request):
    return render(request, 'accounts/demo.html')


def contact_info(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = f"Nouveau message de contact de {name} ."
        full_message = f"Nom: {name} \nEmail: {email} \n\nMessage:\n {message}"
        send_mail(
            subject,
            full_message,
            email,
            ['kpokoutaabel@gmail.com'],
        )

        messages.success(request , " Votre message a bien été envoyé . Merci ! ")
        return render(request,'accounts/successfull_page.html')

    return render(request , 'accounts/contact.html')








