from django.db import models
from django.contrib.auth.models import User


class Scooter(models.Model):
    """
        The scooter class represents the model for scooter rental and presentation in this system
    """

    scooter_model = models.CharField(max_length=255, blank=True, null=True)
    # criar regra para que a data de entrega não pode ser inferior a data do aluguel
    rent_date = models.DateField(blank=True, null=True)
    end_rent_date = models.DateField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)


    def __str__(self):
        return self.scooter_model