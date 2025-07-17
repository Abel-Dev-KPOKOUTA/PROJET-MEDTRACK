from django.db import models
from patients.models import PatientProfile
class Alert(models.Model):

    SEVERITY_CHOICES = [
        ('LOW','Faible'),
        ('MEDIUM','Moyenne'),
        ('HIGH','Haute'),
    ]

    TYPE_CHOICES = [
        ('BP','Tension artérielle'),
        ('APPT','Rendez-vous'),
        ('MED','Médicament')
    ]

    patient = models.ForeignKey(PatientProfile , on_delete=models.CASCADE)
    alert_type = models.CharField(max_length=5 , choices=TYPE_CHOICES)
    severity = models.TextField()
    is_read = models.BooleanField(default= False)
    related_object_id = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def get_icon_class(self):
        icons = {
            'BP':'fas fa-heartbeat',
            'APPT':'fas fa_calendar-alt',
            'MED' : 'fas fa-pills'
        }

        return icons.get(self.alert_type , 'fas fa-bell')
    
    def get_severity_class(self):
        return {
            'LOW':'info',
            'MEDIUM':'warning',
            'HIGH':'danger'
        }.get(self.severity , 'info')
    
    