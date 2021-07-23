from django.db import models
from django.urls import reverse

# Create your models here.

class Signatory(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Request(models.Model):
    time = models.TimeField(auto_now=True)
    date = models.DateField(auto_now=True)
    full_name = models.CharField(max_length=100)
    school_id = models.CharField(max_length=15)
    email = models.EmailField(default='')
    signatory = models.ForeignKey(Signatory, on_delete=models.CASCADE)
    purpose = models.TextField(max_length=300, default='')
    status = models.CharField(max_length=10, default='pending')

    def __str__(self):
        return self.full_name + ' ' + self.school_id

    def get_absolute_url(self):
        return reverse('request_sent')



