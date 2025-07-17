from django.db import models
from django.core.validators import RegexValidator
from accounts.models import CustomUser 
from django.conf import settings
'''
Le patient héritera naturellement de quelques options d'un utilisateur . 
Car logiquement , avant d'être patient , on est d'abord un utilisateur . 
Donc dans le model des patients , il doit y avoir un caratère utilisateur ; donc

PatientProfile(models.Model) : fere un models.OneToOne(CustomUser , on_delete=models.CASCADE)
'''
class PatientProfile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Masculin'),
        ('F', 'Féminin'),
        ('O', 'Autre'),
    ]
    
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='patient_profile'
    )
    phone = models.CharField(
        max_length=15,
        validators=[RegexValidator(r'^\+?1?\d{9,15}$', "Format : '+225...'.")],
        blank=True
    )
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        blank=True,
        verbose_name="Genre"
    )
    date_of_birth = models.DateField(
        null=True,
        blank=True,
        verbose_name="Date de naissance"
    )
    address = models.TextField(blank=True, verbose_name="Adresse")
    medical_history = models.TextField(
        blank=True,
        verbose_name="Antécédents médicaux"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Profil Patient"
        verbose_name_plural = "Profils Patients"
        ordering = ['-created_at']

    def _str_(self):
        return f"{self.user.get_full_name() or self.user.username} (Patient)"

