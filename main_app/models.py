from django.db import models
from django.urls import reverse

# Create your models here.
class Rat(models.Model):
  name = models.CharField(max_length=100)
  color= models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  location = models.CharField(max_length=150)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('rats_detail', kwargs={'rat_id': self.id})