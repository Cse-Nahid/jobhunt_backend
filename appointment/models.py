from django.db import models
from candidate.models import Candidate
from employer.models import Employer, AvailableTime
# Create your models here.

APPOINTMENT_STATUS = [
    ('Completed', 'Completed'),
    ('Pending', 'Pending'),
    ('Running', 'Running'),
]
APPOINTMENT_TYPES = [
    ('Offline', 'Offline'),
    ('Online', 'Online'),
]
class Appointment(models.Model):
    # candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='appointment_from_appointment')
    candidate= models.ForeignKey(Candidate, on_delete = models.CASCADE)
    employer = models.ForeignKey(Employer, on_delete = models.CASCADE)
    appointment_types = models.CharField(choices = APPOINTMENT_TYPES, max_length = 10)
    appointment_status = models.CharField(choices = APPOINTMENT_STATUS, max_length = 10, default = "Pending")
    symptom = models.TextField()
    time = models.OneToOneField(AvailableTime, on_delete = models.CASCADE)
    cancel = models.BooleanField(default = False)
    
    def __str__(self):
        return f"Employer : {self.employer.user.first_name} , Candidate : {self.candidate.user.first_name}"