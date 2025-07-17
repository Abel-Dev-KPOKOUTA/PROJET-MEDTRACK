from django.urls import path 
from .views import (
    DoctorSignUpView, 
    PatientSignUpView, 
    CustomLoginView, 
    CustomLogoutView, 
    accueil_page,
    demonstration,
    contact_info,
    custom_patient_signup,  # <-- Ajoute cette importation
)

app_name = 'accounts'

urlpatterns = [
    path('signup/doctor/', DoctorSignUpView.as_view(), name='doctor_signup'),
    # Remplace la ligne suivante :
    # path('signup/patient/', PatientSignUpView.as_view(), name='patient_signup'),
    # par celle-ci :
    path('signup/patient/', custom_patient_signup, name='patient_signup'),
    path('login/', CustomLoginView.as_view(), name='login_user'),
    path('logout/', CustomLogoutView.as_view(), name='logout_user'),
    path('accueil/',accueil_page , name='accueil'),
    path('demonstration/', demonstration , name='demonstration'),
    path('contact/', contact_info, name='contact'),
]