from django.db import models
from patients.models import PatientProfile
from doctors.models import Doctor

class Appointment(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    duration = models.PositiveSmallIntegerField(default=30)  # en minutes
    location = models.CharField(max_length=200)
    reason = models.TextField()
    is_confirmed = models.BooleanField(default=False)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['date']

    def _str_(self):
        return f"RDV avec Dr. {self.doctor} le {self.date}"