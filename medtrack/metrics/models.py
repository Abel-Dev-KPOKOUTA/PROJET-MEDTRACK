from django.db import models
from patients.models import PatientProfile
# Create your models here.
########### CETTE APPLICATION A ETE CREER POUR LA GESION DE LA TENSION + AUTRES MESURES DES PATIENTS... ##########

class BloodPressure(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, related_name='blood_pressures')
    systolic = models.PositiveSmallIntegerField()
    diastolic = models.PositiveSmallIntegerField()
    pulse = models.PositiveBigIntegerField()
    measured_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['-measured_at']
        verbose_name = "Pression artérielle"

    def __str__(self):
        return f"{self.systolic}/{self.diastolic} - {self.measured_at.strftime('%d/%m/%Y')}"