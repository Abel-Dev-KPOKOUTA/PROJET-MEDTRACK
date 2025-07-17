from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    is_assistant = models.BooleanField(default=False)

    class Meta:
        verbose_name='Utilisateur'
        verbose_name_plural='Utilisateurs'

    def __str__(self):
        return self.username