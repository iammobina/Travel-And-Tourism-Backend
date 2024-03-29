from django.db import models
from django.contrib.auth.models import User

class user(User):
    itinerary=models.CharField(max_length=500)
    is_leader=models.BooleanField(default=False)
    phone_number=models.CharField(max_length=13)
    avatar =models.ImageField(default='/profile/profile.jpg',upload_to='profile')

class TimeOBJ(models.Model):
    startime=models.DateTimeField(null=True)
    endtime=models.DateTimeField(null=True)

class Leader(models.Model):
    userID=models.OneToOneField(user,on_delete=models.CASCADE)
    is_available=models.BooleanField(default=False)
    nationalID=models.CharField(max_length=12)
    has_car=models.BooleanField(default=False)
    car_capacity=models.CharField(max_length=5)
    car_model=models.CharField(max_length=20)
    gender=models.BooleanField(default=False)
    age=models.CharField(max_length=3,default=None)
    freetimes=models.ManyToManyField(TimeOBJ)


class LeaderRate(models.Model):
    user=models.ForeignKey(user,on_delete=models.CASCADE)
    leader=models.ForeignKey(Leader,on_delete=models.CASCADE)
    rate=models.IntegerField(blank=True)
