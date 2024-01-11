from django.db import models
from patient.models import Patient
# Create your models here.
from django.contrib.auth.models import User

class Specialization(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self) -> str:
        return self.name
    
class Designation(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self) -> str:
        return self.name
    
class AvailableTime(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self) -> str:
        return self.name
    


class Doctor(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='doctor/images', null=True, blank=True)
    designation = models.ManyToManyField(Designation)
    specialization = models.ManyToManyField(Specialization)
    AavailableTime = models.ManyToManyField(AvailableTime)
    fee = models.IntegerField()
    meet_ling = models.CharField(max_length=100)



    def __str__(self) -> str:
        return f"Dr. {self.user.first_name} {self.user.last_name}"
    




STR_CHOICES = [
    ('★','★'),
    ('★★','★★'),
    ('★★★','★★★'),
    ('★★★★','★★★★'),
    ('★★★★★','★★★★★'),
]


class Review(models.Model):
    reviewer = models.ForeignKey(Patient, on_delete=models.CASCADE) #jeta multiple hobe sikhane foreign key dawa hoeb
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    rating = models.CharField(choices = STR_CHOICES, max_length =100)


    def __str__(self) -> str:
        return f"Patient : {self.reviewer.user.first_name}, Doctor: {self.doctor.user.first_name}"