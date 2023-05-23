from django.db import models


# Create your models here.

class AppUser(models.Model):
    first_name = models.CharField(max_length=200, blank=False, null=False)
    last_name = models.CharField(max_length=200, blank=False, null=False)
    username = models.CharField(max_length=200, blank=False, null=False, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=15, blank=False, null=False)


class CycleDate(models.Model):
    menstrual_cycle_length = models.IntegerField()
    period_date = models.DateField()
    safe_days = models.DateField()
    fertility_days = models.DateField()
    ovulation_day = models.DateField()

    def __str__(self):
        return self.period_date

