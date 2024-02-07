from django.db import models

# Create your models here.
from Employee_app.models import EmployeePersonal 

class Production(models.Model):
    production_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(EmployeePersonal, on_delete=models.CASCADE)
    product_id = models.CharField(max_length=100, null=False, blank=False)
    production_date = models.DateField(auto_now_add=True)
    shift = models.CharField(max_length=50, null=False, blank=False)
    quantity_produced = models.PositiveIntegerField(null=False, blank=False)
    work_center = models.CharField(max_length=100, null=False, blank=False)
    production_order_id = models.CharField(max_length=100, null=True, blank=True)
    time_in = models.TimeField(null=False, blank=False)
    time_out = models.TimeField(null=False, blank=False)
    production_status = models.CharField(max_length=20, choices=[('in_progress', 'In Progress'), ('completed', 'Completed')])

class Stack(models.Model):
    stack_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(EmployeePersonal, on_delete=models.CASCADE)
    product_id = models.CharField(max_length=100, null=False, blank=False)
    stack_date = models.DateField(auto_now_add=True)
    stack_quantity = models.PositiveIntegerField(null=False, blank=False)
    stack_location = models.CharField(max_length=100, null=False, blank=False)
    stack_order_id = models.CharField(max_length=100, null=True, blank=True)
    stack_notes = models.TextField(null=True, blank=True)
