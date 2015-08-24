import datetime

from django.db import models
from django.utils import timezone


class Weight(models.Model):
    weight = models.IntegerField(default='')
    record_date = models.DateTimeField('date record')

    def __str__(self):
    	return str(self.weight)
