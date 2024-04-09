from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    city = models.CharField(max_length=100)
    address = models.TextField()

    class Meta:
        app_label = 'api'  # Specify the app label

    def __str__(self):
        return self.name

class Vacancy(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    salary = models.FloatField()
    company = models.ForeignKey('api.Company', on_delete=models.CASCADE, related_name='vacancies')  # Specify the related model using string

    class Meta:
        app_label = 'api'  # Specify the app label

    def __str__(self):
        return self.name
