from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='s')
    image = models.ImageField(upload_to='service/images',null=True, blank=True)