from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import PatientProfile
from .forms import PatientProfileForm
from accounts.models import CustomUser
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from metrics.models import BloodPressure
from alerts.models import Alert 
from appointments.models import Appointment
from django.utils import timezone
from treatments.models import Treatment

class PatientCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = PatientProfile
    form_class = PatientProfileForm
    template_name = 'patients/patient_form.html'
    success_url = '/patients/list/'

    def test_func(self):
        return self.request.user.is_doctor or self.request.user.is_superuser

    def form_valid(self, form):
        form.instance.user = CustomUser.objects.create_user(
            username=form.cleaned_data['phone'],  # ou générer un username unique
            is_patient=True
        )
        return super().form_valid(form)

class PatientListView(LoginRequiredMixin, ListView):
    model = PatientProfile
    template_name = 'patients/patient_list.html'
    context_object_name = 'patients'
    paginate_by = 10

    def get_queryset(self):
        return PatientProfile.objects.select_related('user').order_by('-created_at')
    


'''
@login_required
def patient_dashboard(request):
    # Remplace par le modèle de symptômes si tu en as un
    symptomes = []  # Par exemple : Symptom.objects.filter(patient=request.user.patient_profile).order_by('-date')
    critical_alert = None  # Ajoute une logique si besoin

    if request.method == "POST":
        description = request.POST.get("description")
        if description:
            # Symptom.objects.create(patient=request.user.patient_profile, description=description)
            pass
        return redirect('patients:dashboard')

    return render(request, 'patients/dashboard.html', {
        'symptomes': symptomes,
        'critical_alert': critical_alert
    })
'''

@login_required
def patient_dashboard(request):
    try :
        patient = request.user.patient_profile
    except PatientProfile.DoesNotExist :
        patient = None 
    context = {
        'latest_bp': BloodPressure.objects.filter(patient=patient).first(),
        'unread_alerts': Alert.objects.filter(patient=patient, is_read=False),
        'next_appointment': Appointment.objects.filter(
            patient=patient,
            date__gte= timezone.now()
        ).order_by('date').first(),
        'active_treatments': Treatment.objects.filter(patient = patient , is_active=True)
    }

    return render(request,'patients/dashboard.html',context)



def attente_profile(request):
    return render(request,'patients/profil.html')


def attente_document(request):
    return render(request,'patients/documents.html')


def attente_medecins(request):
    return render(request,'patients/medecins.html')


def attente_traitements(request):
    return render(request,'patients/traitements.html')

def historique(request):
    return render(request , 'patients/historique.html')

def rendez_vous(request):
    return render(request, 'patients/rendez_vous.html')