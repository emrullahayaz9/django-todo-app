from django.db import models
from django.forms import ModelForm


# Create your models here.

class todoModel(models.Model):
    header = models.CharField(max_length=100)
    content = models.TextField()

class todoModelForm(ModelForm):
    class Meta:
        model=todoModel
        fields="__all__"
