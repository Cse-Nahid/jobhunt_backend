from django.db import models
from django.contrib.auth.models import User
# from candidate.models import employer

# Create your models here.

# {
#     "title": "Software Engineer",
#     "description": "Develop and maintain software applications.",
#     "requirements": "Bachelor's degree in Computer Science, 2+ years of experience.",
#     "location": "New York, NY"
# }

from django.db import models

class Employer(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    requirements = models.TextField()
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class AvailableTime(models.Model):
    name = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.name

# STAR_CHOICES = [
#     ('⭐', '⭐'),
#     ('⭐⭐', '⭐⭐'),
#     ('⭐⭐⭐', '⭐⭐⭐'),
#     ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
#     ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
# ]
# class Review(models.Model):
#     reviewer = models.ForeignKey(Patient, on_delete = models.CASCADE)
#     # doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)
#     body = models.TextField()
#     created = models.DateTimeField(auto_now_add = True)
#     rating = models.CharField(choices = STAR_CHOICES, max_length = 10)
    
#     def __str__(self):
#         return f"Patient : {self.reviewer.user.first_name} ; Doctor {self.doctor.user.first_name}"