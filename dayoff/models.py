from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    reason = models.CharField(max_length=1000)
    offtype=(
        ('ลากิจ','ลากิจ'),
        ('ลาป่วย', 'ลาป่วย'),
    )
    type = models.CharField(max_length=20,choices=offtype)
    date_start = models.DateField()
    date_end = models.DateField()

    status = (
        ('รอการอณุมัติ', 'รอการอณุมัติ'),
        ('อณุมัติ', 'อณุมัติ'),
        ('ไม่อณุมัติ', 'ไม่อณุมัติ'),
    )
    approve_status = models.CharField(max_length=30,choices=status)