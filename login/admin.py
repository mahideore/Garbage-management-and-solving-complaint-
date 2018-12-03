# -*- coding: utf-8 -*-
from .models import UserComplaint,UserWifiComplaint,UserCivilComplaint,UserElectricComplaint,UserMachanicalComplaint,UserOtherComplaint,WifiComplaintWorker,CivilComplaintWorker,ElectricComplaintWorker,OtherComplaintWorker,WifiComplaintDetails,CivilComplaintDetails,ElectricComplaintDetails,OtherComplaintDetails
#from .models import *
from django.contrib import admin

class UserComplaintAdmin(admin.ModelAdmin):
    list_display = ('user', 'complaint', 'location', 'Mobile_number', 'pub_date')

admin.site.register(UserComplaint, UserComplaintAdmin)


class UserWifiComplaintAdmin(admin.ModelAdmin):
    list_display = ('user', 'complaint','location','bulding_name','room_number','Mobile_number','email','status', 'pub_date')
admin.site.register(UserWifiComplaint, UserWifiComplaintAdmin)

class UserCivilComplaintAdmin(admin.ModelAdmin):
    list_display = ('user', 'complaint','location','bulding_name','room_number','Mobile_number','email','status', 'pub_date')
admin.site.register(UserCivilComplaint, UserCivilComplaintAdmin)

class UserElectricComplaintAdmin(admin.ModelAdmin):
    list_display = ('user', 'complaint','location','bulding_name','room_number','Mobile_number','email','status', 'pub_date')
admin.site.register(UserElectricComplaint, UserElectricComplaintAdmin)

class UserMachanicalComplaintAdmin(admin.ModelAdmin):
    list_display = ('user', 'complaint','location','bulding_name','room_number','Mobile_number','email','status', 'pub_date')
admin.site.register(UserMachanicalComplaint, UserMachanicalComplaintAdmin)

class UserOtherComplaintAdmin(admin.ModelAdmin):
    list_display = ('user', 'complaint','location','bulding_name','room_number','Mobile_number','email','status', 'pub_date')
admin.site.register(UserOtherComplaint, UserOtherComplaintAdmin)

class WifiComplaintWorkerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'middle_name', 'last_name', 'Mobile_number', 'email','pub_date')
admin.site.register(WifiComplaintWorker, WifiComplaintWorkerAdmin)

class CivilComplaintWorkerAdmin(admin.ModelAdmin): 
    list_display = ('first_name', 'middle_name', 'last_name', 'Mobile_number', 'email','pub_date')
admin.site.register(CivilComplaintWorker, CivilComplaintWorkerAdmin)


class ElectricComplaintWorkerAdmin(admin.ModelAdmin): 
    list_display = ('first_name', 'middle_name', 'last_name', 'Mobile_number', 'email','pub_date')
admin.site.register(ElectricComplaintWorker, ElectricComplaintWorkerAdmin)

class OtherComplaintWorkerAdmin(admin.ModelAdmin): 
    list_display = ('first_name', 'middle_name', 'last_name', 'Mobile_number', 'email','pub_date')
admin.site.register(OtherComplaintWorker, OtherComplaintWorkerAdmin)

class WifiComplaintDetailsAdmin(admin.ModelAdmin): 
       list_display = ('user','user_complaint','user_location','user_Mobile_number','email','worker_name','worker_Mobile_number','status','pub_date')
admin.site.register(WifiComplaintDetails, WifiComplaintDetailsAdmin)


class CivilComplaintDetailsAdmin(admin.ModelAdmin): 
       list_display = ('user','user_complaint','user_location','user_Mobile_number','email','worker_name','worker_Mobile_number','status','pub_date')
admin.site.register(CivilComplaintDetails, CivilComplaintDetailsAdmin)


class ElectricComplaintDetailsAdmin(admin.ModelAdmin): 
       list_display = ('user','user_complaint','user_location','user_Mobile_number','email','worker_name','worker_Mobile_number','status','pub_date')
admin.site.register(ElectricComplaintDetails, ElectricComplaintDetailsAdmin)


class OtherComplaintDetailsAdmin(admin.ModelAdmin): 
       list_display = ('user','user_complaint','user_location','user_Mobile_number','email','worker_name','worker_Mobile_number','status','pub_date')
admin.site.register(OtherComplaintDetails, OtherComplaintDetailsAdmin)




