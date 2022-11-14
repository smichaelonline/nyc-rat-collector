from django.db import models
from django.urls import reverse
from datetime import date

MEALS = (
  ('B', 'Breakfast'),
  ('L', 'Lunch'),
  ('D', 'Dinner')
)

class Trait(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('traits_detail', kwargs={'pk': self.id})

class Rat(models.Model):
  name = models.CharField(max_length=100)
  color= models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  location = models.CharField(max_length=150)
  traits = models.ManyToManyField(Trait)

  def fed_for_today(self):
    return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('rats_detail', kwargs={'rat_id': self.id})

class Feeding(models.Model):
  date = models.DateField('Feeding date')
  meal = models.CharField(
    max_length=1,
    choices=MEALS,
    default=MEALS[0][0])

  rat = models.ForeignKey(Rat, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"

  class Meta:
    ordering = ['-date']
