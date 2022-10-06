from django.db import models
from django.db.models import Model

# Create your models here.
class Thing(Model):
    name = models.CharField(max_length=30, unique=True, blank=False)
    description = models.TextField(max_length=120)
    quantity = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
