from django.forms import ModelForm
from .models import Season

class SeasonForm(ModelForm):
  class Meta:
    model = Season
    fields = ['date', 'season']