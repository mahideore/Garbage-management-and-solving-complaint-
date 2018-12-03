from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db import migrations



class UserComplaint(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    complaint = models.CharField(max_length=200)
    location = models.CharField(max_length=200, default="Null")
    Mobile_number = models.IntegerField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.location



class UserWifiComplaint(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    first_name=models.CharField(max_length=200 ,null=True)
    complaint = models.CharField(max_length=200)
    location = models.CharField(max_length=200, default="Null")
    bulding_name=models.TextField(max_length=200 ,default="Null")
    room_number=models.TextField(null=True)
    Mobile_number = models.IntegerField(null=True)
    email=models.EmailField(null=True)
    status =  models.BooleanField(default=False)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        
        return unicode(self.user)
    



class UserCivilComplaint(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    complaint = models.CharField(max_length=200)
    location = models.CharField(max_length=200, default="Null")
    bulding_name=models.TextField(max_length=200 ,default="Null")
    room_number=models.TextField(null=True)
    Mobile_number = models.IntegerField()
    email=models.EmailField(null=True)
    status =  models.BooleanField(default=False)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.location

class UserElectricComplaint(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    complaint = models.CharField(max_length=200)
    location = models.CharField(max_length=200, default="Null")
    bulding_name=models.TextField(max_length=200 ,default="Null")
    room_number=models.TextField(null=True)
    Mobile_number = models.IntegerField()
    email=models.EmailField(null=True)
    status =  models.BooleanField(default=False)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.location


class UserMachanicalComplaint(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    complaint = models.CharField(max_length=200)
    location = models.CharField(max_length=200, default="Null")
    bulding_name=models.TextField(max_length=200 ,default="Null")
    room_number=models.TextField(null=True)
    Mobile_number = models.IntegerField()
    email=models.EmailField(null=True)
    status =  models.BooleanField(default=False)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.location

class UserOtherComplaint(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    complaint = models.CharField(max_length=200)
    location = models.CharField(max_length=200, default="Null")
    bulding_name=models.TextField(max_length=200 ,default="Null")
    room_number=models.TextField(null=True)
    Mobile_number = models.IntegerField()
    email=models.EmailField(null=True)
    status =  models.BooleanField(default=False)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.location

class WifiComplaintWorker(models.Model):
    first_name = models.CharField(max_length=200, default="Null")
    middle_name = models.CharField(max_length=200,default="Null")
    last_name = models.CharField(max_length=200, default="Null")
    Mobile_number = models.IntegerField()
    email=models.EmailField(null=True)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.first_name + self.last_name 

class CivilComplaintWorker(models.Model):
    first_name = models.CharField(max_length=200, default="Null")
    middle_name = models.CharField(max_length=200,default="Null")
    last_name = models.CharField(max_length=200, default="Null")
    Mobile_number = models.IntegerField()
    email=models.EmailField(null=True)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.first_name

class ElectricComplaintWorker(models.Model):
    first_name = models.CharField(max_length=200, default="Null")
    middle_name = models.CharField(max_length=200,default="Null")
    last_name = models.CharField(max_length=200, default="Null")
    Mobile_number = models.IntegerField()
    email=models.EmailField(null=True)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.first_name

class OtherComplaintWorker(models.Model):
    first_name = models.CharField(max_length=200, default="Null")
    middle_name = models.CharField(max_length=200,default="Null")
    last_name = models.CharField(max_length=200, default="Null")
    Mobile_number = models.IntegerField()
    email=models.EmailField(null=True)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.first_name


class WifiComplaintDetails(models.Model):
    user= models.ForeignKey(User, null=True, blank=True)
    first_name = models.CharField(max_length=200, default="some string")
    user_complaint = models.CharField(max_length=200)
    user_location = models.CharField(max_length=200, default="Null")
    user_Mobile_number = models.IntegerField()
    email=models.EmailField(null=True)
    WifiComplaintWorker = models.ForeignKey(WifiComplaintWorker,null=True) 
    worker_name= models.CharField(max_length=200,default="Null")
    last_name = models.CharField(max_length=200, default="Null")
    worker_Mobile_number = models.IntegerField(null=True)
    pub_date = models.DateTimeField('date published')
    status = models.BooleanField(default=False)

       


    def __str__(self):
        return self.first_name
        
class CivilComplaintDetails(models.Model):
    user= models.ForeignKey(User, null=True, blank=True)
    first_name = models.CharField(max_length=200, default="some string")
    user_complaint = models.CharField(max_length=200)
    user_location = models.CharField(max_length=200, default="Null")
    user_Mobile_number = models.IntegerField()
    email=models.EmailField(null=True)
    CivilComplaintWorker = models.ForeignKey(CivilComplaintWorker,null=True) 
    worker_name= models.CharField(max_length=200,default="Null")
    last_name = models.CharField(max_length=200, default="Null")
    worker_Mobile_number = models.IntegerField(null=True)
    pub_date = models.DateTimeField('date published')
    status = models.BooleanField(default=False)


       


    def __str__(self):
        return self.location 
        

class ElectricComplaintDetails(models.Model):
    user= models.ForeignKey(User, null=True, blank=True)
    first_name = models.CharField(max_length=200, default="some string")
    user_complaint = models.CharField(max_length=200)
    user_location = models.CharField(max_length=200, default="Null")
    user_Mobile_number = models.IntegerField()
    email=models.EmailField(null=True)
    ElectricComplaintWorker = models.ForeignKey(ElectricComplaintWorker,null=True) 
    worker_name= models.CharField(max_length=200,default="Null")
    last_name = models.CharField(max_length=200, default="Null")
    worker_Mobile_number = models.IntegerField(null=True)
    pub_date = models.DateTimeField('date published')
    status = models.BooleanField(default=False)


       


    def __str__(self):
        return self.location 
        
class OtherComplaintDetails(models.Model):
    user= models.ForeignKey(User, null=True, blank=True)
    first_name = models.CharField(max_length=200, default="some string")
    user_complaint = models.CharField(max_length=200)
    user_location = models.CharField(max_length=200, default="Null")
    user_Mobile_number = models.IntegerField()
    email=models.EmailField(null=True)
    OtherComplaintWorker = models.ForeignKey(OtherComplaintWorker,null=True) 
    worker_name= models.CharField(max_length=200,default="Null")
    last_name = models.CharField(max_length=200, default="Null")
    worker_Mobile_number = models.IntegerField(null=True)
    pub_date = models.DateTimeField('date published')
    status = models.BooleanField(default=False)


    def __str__(self):
        return self.location 
