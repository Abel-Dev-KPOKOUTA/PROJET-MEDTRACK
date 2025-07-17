from django.urls import path , include
from .views import PatientListView 
from .import views

app_name = 'patients'
urlpatterns = [
    path('list/' , PatientListView.as_view() , name='patient_list'),
    path("dashboard/", views.patient_dashboard, name="dashboard"),
    path('attentes/profil', views.attente_profile , name='profile'),
    path('attentes/medecins', views.attente_medecins , name='medecins'),
    path('attentes/traitements' , views.attente_traitements , name ='traitements'),
    path('attentes/documents' , views.attente_document , name ='documents'),
    path('attentes/historique', views.historique , name ='historique'),
    path('attentes/rendez_vous/',views.rendez_vous , name='RDV'),
    ]
