from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Candidate(models.Model):
    title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)  # New field
    description = models.TextField()
    requirements = models.TextField()
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Appointment2(models.Model):
   candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
