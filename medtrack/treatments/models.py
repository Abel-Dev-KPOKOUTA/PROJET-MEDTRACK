from django.db import models
from patients.models import PatientProfile

class Treatment(models.Model):
    patient = models.ForeignKey(
        PatientProfile, 
        on_delete=models.CASCADE,
        related_name='treatments'
    )
    medication = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
    frequency = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    # ... autres champs