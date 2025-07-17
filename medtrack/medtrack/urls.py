from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('doctors/', include('doctors.urls')),
    path('patients/' , include('patients.urls')),
    path('symptoms/', include('symptoms.urls')),
    path('alerts/', include('alerts.urls')),
    path('appointments/', include('appointments.urls')),
    path('documents/', include('documents.urls')),
    path('metrics/', include('metrics.urls')),
    path('treatments/', include('treatments.urls')),
]
