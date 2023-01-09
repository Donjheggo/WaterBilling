from django.db import models
from account.models import *
import datetime
import string, secrets


class Client(models.Model):
    meter_number = models.BigIntegerField(null=True)
    first_name = models.CharField(max_length=30) 
    last_name = models.CharField(max_length=30) 
    middle_name = models.CharField(max_length=30, null=True, blank=True) 
    contact_number = models.CharField(null=True, unique=True, max_length=13)
    address = models.CharField(max_length=250)
    status = models.TextField(choices=(('Connected', 'Connected'), ('Disconnected', 'Disconnected'), ('Pending', 'Pending')))


    def __str__(self):
        if self.middle_name:
            return f"{self.last_name}, {self.first_name} {self.middle_name}"
        else:
            return f"{self.last_name}, {self.first_name}"


class WaterBill(models.Model):
    name = models.ForeignKey(Client, on_delete=models.CASCADE)
    meter_consumption = models.BigIntegerField(null=True)
    status = models.TextField(choices=(('Paid','Paid'),('Pending', 'Pending')), null=True)
    duedate = models.DateField(null=True)
    penaltydate = models.DateField(null=True)

    
    def compute_bill(self):
        metric = Metric.objects.get(id=1)
        consump_amount = metric.consump_amount
        return self.meter_consumption * consump_amount

    def penalty(self):
        if self.penaltydate == datetime.date.today():
            metric = Metric.objects.get(id=1)
            penalty_cost = metric.penalty_amount
            return penalty_cost
        else:
            return 0

    
    def payable(self):
        if self.penalty:
            return self.compute_bill() + self.penalty()
        else:
            return self.compute_bill()


    def __str__(self):
        return f'{self.name}'


class Metric(models.Model):
    consump_amount = models.FloatField(default=1, null=True)
    penalty_amount = models.FloatField(default=1, null=True)