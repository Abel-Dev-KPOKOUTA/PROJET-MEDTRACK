from django.db import models
from patients.models import PatientProfile

'''
Pour avoir les symptomes ont doit naturellement se pointer sur un patient . Donc c'est que c'est 
grace aux patients qu'on peut avoir les symptomes pour causes de maladies et on s'en passe...
'''

class SymptomReport(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    description = models.TextField()
    severity = models.CharField(max_length=50 , choices=[
        ('light','Léger'),
        ('moderate','Modéré'),
        ('severe','Sévère'),
    ])
    date_reported= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.patient.user.username} - {self.date_reported.date()}'