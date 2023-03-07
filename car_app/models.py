from django.db import models
import uuid
from datetime import datetime
# Create your models here.

class CarInfo(models.Model):
    car_no = models.TextField()


