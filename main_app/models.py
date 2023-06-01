from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


# A tuple of 2-tuples
SEASON = (
  ('F', 'Fall'),
  ('W', 'Winter'),
  ('Su', 'Summer'),
  ('Sp', 'Spring')
)



# Create your models here.

class Pref(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)


class Tree(models.Model):
  name = models.CharField(max_length=100)
  family = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  lifeSpan = models.IntegerField()
  prefs = models.ManyToManyField(Pref)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('tree-detail', kwargs={'tree_id': self.id})
  
  def fed_for_today(self):
    return self.season_set.filter(date=date.today()).count() >= len(SEASON)

class Season(models.Model):
  date = models.DateField('Season date')
  season = models.CharField(
  max_length=2,
  choices=SEASON,
  default=SEASON[0][0]
  )
  tree = models.ForeignKey(Tree, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_season_display()} on {self.date}"
  
  class Meta:
    ordering = ['-date']

  def __str__(self):
    return self.date

  def get_absolute_url(self):
    return reverse('pref-detail', kwargs={'pk': self.id})