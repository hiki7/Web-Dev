from django.db import models
from rest_framework import serializers
# Create your models here.
class Company(models.Model):
    def __str__(self):
        return f'{self.name}'
    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
    def to_json(self):
        return{
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address
        }
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1000,default='')
    city = models.CharField(max_length=255,default='')
    address = models.TextField(max_length=1000,default='')
class Vacancy(models.Model):
    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'
    def __str__(self):
        return f'{self.name}'
    def to_json(self):
        return{
            'name': self.name,
            'description': self.description,
            'salary': self.salary,
            # 'company': self.company
        }
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1000,default='')
    salary = models.FloatField(default=1000)
    company = models.ForeignKey("Company",on_delete=models.CASCADE,default=0)