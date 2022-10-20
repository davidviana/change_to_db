from django.db import models

# Create your models here.


class Pokemons(models.Model):
    Stripe = models.ImageField()
    Name = models.CharField(max_length=80)
    Total_Status = models.IntegerField()
    Primary_Type = models.CharField(max_length=80)
    Secundary_Type = models.CharField(max_length=80)
    Status_Base_hp = models.IntegerField()
    Status_Base_attack = models.IntegerField()
    Status_Base_defense = models.IntegerField()
    Status_Special_attack = models.IntegerField()
    Status_Special_defense = models.IntegerField()
    Speed = models.IntegerField()
    Generation = models.CharField(max_length=1)
    Is_Legendary = models.BooleanField()
