from __future__ import unicode_literals
from django.conf import settings
from .form import UserLoginForm, UserRegisterForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from .models import UserComplaint,UserWifiComplaint,UserCivilComplaint,UserElectricComplaint,UserMachanicalComplaint,UserOtherComplaint,WifiComplaintWorker,CivilComplaintWorker,ElectricComplaintWorker,OtherComplaintWorker,WifiComplaintDetails, CivilComplaintDetails,ElectricComplaintDetails,OtherComplaintDetails
from django.core.mail import send_mail,EmailMessage,EmailMultiAlternatives
import datetime, json
import googlemaps
import csv
import socket
from django.contrib.gis.geoip import GeoIP
from django.template.loader import get_template
from django.template.loader import render_to_string
from django.utils.html import strip_tags

#from django.contrib.gis.utils import GeoIP
#from ipware.ip import get_ip_address_from_request
#key to access google api
#api_key = "AIzaSyCGR8OXmOKi4QRktBtuY3YVGbKuW84ypUs"
api_key = "AIzaSyBmrEiwFRhjX5UNe03odV-MGa8NWy3KSZg"
#home page of the website
def index_view(request):
        return render(request, "login/indexx.html", {})
def st_view(request):
        return render(request, "login/status.html", {})
def wf_view(request):
        return render(request, "login/wf.html", {})
def cv_view(request):
        return render(request, "login/cv.html", {})
def ot_view(request):
        return render(request, "login/ot.html", {})
def el_view(request):
        return render(request, "login/el.html", {})


def loct(request):
        return render(request, "login/loct.html", {})
def loc_view(request):    
        return render(request, "login/loc.html", {})

def home_view(request):
        return render(request, "login/homes.html", {})
def wifi_worker_comp(request):
        return render(request, "login/wifi_worker.html", {})
def civil_worker_comp(request):
        return render(request, "login/civil_worker.html", {})
def electric_worker_comp(request):
        return render(request, "login/wifi_worker.html", {})
def other_worker_comp(request):
        return render(request, "login/wifi_worker.html", {})


#login page 
def login_view(request):
    print "inside login view"
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print username, password, "username and password"
        user = authenticate(username=username, password=password)
        print username
        print password
        form = User(request.POST)
        if user is not None:
            if user.is_active:
                login(request, user)
                message="congradulations!!!!!Your Login Successfully "
                try:
                    if WifiComplaintWorker.objects.filter(Mobile_number=username).exists():
                        message="welcome worker Login Successfully "
                        print message
                        return HttpResponseRedirect('/wff/',{"username": username, "msg": message})
                    if CivilComplaintWorker.objects.filter(Mobile_number=username).exists():
                        message="welcome worker Login Successfully "
                        print message
                        return HttpResponseRedirect('/cw/',{"username": username, "msg": message})
                    if ElectricComplaintWorker.objects.filter(Mobile_number=username).exists():
                        message="welcome worker Login Successfully "
                        print message
                        return HttpResponseRedirect('/ew/',{"username": username, "msg": message})
                    if OtherComplaintWorker.objects.filter(Mobile_number=username).exists():
                        message="welcome worker Login Successfully "
                        print message
                        return HttpResponseRedirect('/ow/',{"username": username, "msg": message})
                except:
                    pass
                return HttpResponseRedirect('/profile/',{"username": username, "msg": message})
            else:
                return render(request, 'login/lnn.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'login/lnn.html', {'error_message': 'Enter correct username or password'})
    return render(request, "login/lnn.html", {})

#registration page
@csrf_exempt
def register_view(request):
    title = "Register"
    form = UserRegisterForm(request.POST)
    if form.is_valid():
        user = form.save(commit=False)
        email = form.cleaned_data.get('email')
        usern = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user.set_password(password)
        authenticate(username=user.username, password=password)
        user.is_active = True
        user.save()
        
        message = "Congradulations!!! Your Registrations Completed"
        #from_email = settings.EMAIL_HOST_USER
        #to_email = [email]
        #subject = "from djnago"
        #email = EmailMessage(subject,message,from_email,to_email)
        #email.send()
        #msg="okayyyyy"
        return render(request, "login/registration.html", {"title": title, "email":email, "username": usern, "msg": message})
         
    
    
    context = {
              "form": form,
               "title": title,
               
        
        }
    return render(request, "login/registration.html",context)



    
def reset_password(request):
    if request.method == "POST":
        date_time = datetime.datetime.now()
        varr = request.POST
        variablee = "llllllll"
        print " ", varr
        print varr["password"]
        print varr["username"]
        var=varr["username"]
        var1=varr["password"]
        var2=varr["email"]
        var3=varr["confirm password"]
        print var2
        print var
        print var3
        u = User.objects.get(username=var)
        if var2==u.email:
            
            if var1==var3:
               print u.email
               u.set_password(var1)
               u.save()
               from_email = settings.EMAIL_HOST_USER
               to_email = [u.email]
               subject = "from djnago password confirmation"
               temp=get_template("login/ss.html").render()
               email = EmailMultiAlternatives(subject,temp,from_email,to_email)               
               email.attach_alternative(temp, "text/html")
               email.send()
               msg="Hello your password change Successfully!!!please check your mail as well"
               return render(request, "login/reset.html", {'msg':msg})
            else: 
                msg="Sorry your password and confirm password does not match please try again!!"
                return render(request, "login/reset.html", {'msg':msg})  
        else:
                msg="sorry your registered mail and this mail not same means your mail incorrect please try again "
                return render(request, "login/reset.html", {'msg':msg}) 

    
    return render(request, "login/reset.html", {})

    
    
    
    

#logout user from his profile to the homePage
def logout_view(request):
    logout(request)
    return render(request, "login/index.html", {})


#profile page for the users
def profile_view(request):
    if request.method == "POST":
        date_time = datetime.datetime.now()
        varr = request.POST
        variablee = "lllllllllllllllllllllllllllllllllllllllllllll"
        print "ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo", varr
        
        data_update = UserComplaint(user=request.user, complaint=varr["complaint"], location=varr["location"], Mobile_number=varr["mobile_number"], pub_date=date_time )
        data_update.save()
        message= "complain has been submitted"
        return render(request, 'login/profile.html', {'msg':message})

    return render(request, 'login/profile.html', {})


def display_civil_location(request):
    print "inside"
    #user_ip = get_ip_address_from_request(request)
    user_name=socket.gethostname()
    print user_name
    user_ip=socket.gethostbyname(socket.getfqdn())
    print user_ip

    data = UserCivilComplaint.objects.all()
    loc_list =[]
    details_list = []
    for i in data:
        #print i.user
        #print i.location
        #print loc_list
    
        gmaps = googlemaps.Client(key=api_key)
        address = str(user_ip)
        #address = i(user_ip)
        lat_lng = gmaps.geocode(address)
        # print lat_lng
        loc_list.append(str(user_ip),lat_lng[0]['geometry']['location']['lat'], lat_lng[0]['geometry']['location']['lng'])
        details_list.append([i.Mobile_number, i.complaint, str(i.pub_date)])
        print loc_list
    print details_list
    

    test = loc_list
    print test

    return render_to_response('login/location.html', {"test":json.dumps(test),"listt":json.dumps(details_list) } )
def current_location():

    #return current location
    return 1
def display_wifi_location(request):
    print "inside"
    data = UserWifiComplaint.objects.all()
    loc_list =[]
    details_list = []
    for i in data:
        #print i.user
        #print i.location
        #print loc_list
    
        gmaps = googlemaps.Client(key=api_key)
        address = i.location
        lat_lng = gmaps.geocode(address)
        # print lat_lng
        loc_list.append([i.location,lat_lng[0]['geometry']['location']['lat'], lat_lng[0]['geometry']['location']['lng']
        ])
        details_list.append([i.Mobile_number, i.complaint, str(i.pub_date)])
    # print loc_list
    print details_list


    test = loc_list

    return render_to_response('login/location.html', {"test":json.dumps(test),"listt":json.dumps(details_list) } )

def display_other_location(request):
    print "inside"
    data = UserOtherComplaint.objects.all()
    loc_list =[]
    details_list = []
    for i in data:
        #print i.user
        #print i.location
        #print loc_list
    
        gmaps = googlemaps.Client(key=api_key)
        address = i.location
        lat_lng = gmaps.geocode(address)
        # print lat_lng
        loc_list.append([i.location,lat_lng[0]['geometry']['location']['lat'], lat_lng[0]['geometry']['location']['lng']
        ])
        details_list.append([i.Mobile_number, i.complaint, str(i.pub_date)])
    # print loc_list
    print details_list

    test = loc_list

    return render_to_response('login/location.html', {"test":json.dumps(test),"listt":json.dumps(details_list) } )


def display_electric_location(request):
    print "inside"
    data = UserElectricComplaint.objects.all()
    loc_list =[]
    details_list = []
    for i in data:
        #print i.user
        #print i.location
        #print loc_list
    
        gmaps = googlemaps.Client(key=api_key)
        address = i.location
        lat_lng = gmaps.geocode(address)
        # print lat_lng
        loc_list.append([i.location,lat_lng[0]['geometry']['location']['lat'], lat_lng[0]['geometry']['location']['lng']
        ])
        details_list.append([i.Mobile_number, i.complaint, str(i.pub_date)])
    # print loc_list
    print details_list


    test = loc_list

    return render_to_response('login/location.html', {"test":json.dumps(test),"listt":json.dumps(details_list) } )
def wifi_view(request):
    if request.method == "POST":
        date_time = datetime.datetime.now()
        varr = request.POST
        variablee = "lllllllllllllll"
        print "oooooooooooooooooooooooo", varr
        data_update = UserWifiComplaint(user=request.user, complaint=varr["complaint"], location=varr["location"],bulding_name=varr["bulding_name"],room_number=varr["room_number"], Mobile_number=varr["mobile_number"],email=request.user.email,pub_date=date_time,status = True )
        data_update.save()
        wifi_work_data()
        #message = "Congradulations !!!!your complete has been recieved after 2 days specific wifiworker coming to your exact location"'''
        #from_email = settings.EMAIL_HOST_USER
        #to_email = [request.user.email]
        #subject = "from djnago"
        #temp=get_template("login/sss.html").render()
        #email = EmailMultiAlternatives(subject,temp,from_email,to_email)
        #email = EmailMessage(subject,text_content,from_email,to_email)
        #email.attach_alternative(temp, "text/html")

        #email.send()
        #from_email = settings.EMAIL_HOST_USER
        #to_email = [request.user.email]
        #subject = "from djnago"
        #temp=get_template("login/wifi.html").render()
        
       # email = EmailMultiAlternatives(subject,temp,from_email,to_email)
        #email.attach_alternative(temp, "text/html")
        #email.send()
        #message= "Congradulations!!! Your complaint has been submitted"
        #return render(request, 'login/profile1.html', {'msg':message})
        data=WifiComplaintDetails.objects.all()
        userr= data[len(data) - 1].user
        worker= data[len(data) - 1].worker_name
        contact= data[len(data) - 1].worker_Mobile_number
        location= data[len(data) - 1].user_location
        comp=data[len(data) - 1].user_complaint
        
        #from_email = settings.EMAIL_HOST_USER
        #to_email = [request.user.email]
        #subject = "from djnago"
        #temp=get_template("login/sss.html").render()
        #email = EmailMultiAlternatives(subject,temp,from_email,to_email)
        #email.attach_alternative(temp, "text/html")
        #email.send()
        
        #return render(request, 'login/profile1.html', {})
        
        return render(request, 'login/wifi.html', {'user':userr, 'worker':worker ,'contact':contact ,'location':location ,'comp':comp})   
        

    return render(request, 'login/profile1.html', {})
    



def civil_view(request):
    if request.method == "POST":
        date_time = datetime.datetime.now()
        
        data=UserWifiComplaint.objects.all()
        
        varr = request.POST
        variablee = "lllllllllllllllllllllllllllllllllllllllllllll"
        print "ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo", varr
        
        data_update = UserCivilComplaint(user=request.user, complaint=varr["complaint"], location=varr["location"],bulding_name=varr["bulding_name"],room_number=varr["room_number"], Mobile_number=varr["mobile_number"],pub_date=date_time,status = True )
        data_update.save()
        civil_work_data()
        message = "Congradulations !!!!your complete has been recieved after 2 days specific Civilworker coming to your exact location"
        from_email = settings.EMAIL_HOST_USER
        to_email = [request.user.email]
        subject = "from djnago"
        email = EmailMessage(subject,message,from_email,to_email)
        email.send()
        data=CivilComplaintDetails.objects.all()
        userr= data[len(data) - 1].user
        worker= data[len(data) - 1].worker_name
        contact= data[len(data) - 1].worker_Mobile_number
        location= data[len(data) - 1].user_location
        comp=data[len(data) - 1].user_complaint
        return render(request, 'login/civil.html', {'user':userr, 'worker':worker ,'contact':contact ,'location':location ,'comp':comp})   

        #return render(request, 'login/wifi.html', {'user':userr, 'worker':worker ,'contact':contact ,'location':location ,'comp':comp})   

        

    return render(request, 'login/profile2.html', {})

def electric_view(request):
    if request.method == "POST":
        date_time = datetime.datetime.now()
        varr = request.POST
        variablee = "lllllllllllllllllllllllllllllllllllllllllllll"
        print "ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo", varr
        
        data_update = UserElectricComplaint(user=request.user, complaint=varr["complaint"], location=varr["location"],bulding_name=varr["bulding_name"],room_number=varr["room_number"], Mobile_number=varr["mobile_number"],pub_date=date_time,status = True )
        data_update.save()
        electric_work_data()
        message = "Congradulations !!!!your complete has been recieved after 2 days specific Electricworker coming to your exact location"
        from_email = settings.EMAIL_HOST_USER
        to_email = [request.user.email]
        subject = "from djnago"
        email = EmailMessage(subject,message,from_email,to_email)
        email.send()
        data=ElectricComplaintDetails.objects.all()
        userr= data[len(data) - 1].user
        worker= data[len(data) - 1].worker_name
        contact= data[len(data) - 1].worker_Mobile_number
        location= data[len(data) - 1].user_location
        comp=data[len(data) - 1].user_complaint
        return render(request, 'login/electric.html', {'user':userr, 'worker':worker ,'contact':contact ,'location':location ,'comp':comp})   

        #return render(request, 'login/wifi.html', {'user':userr, 'worker':worker ,'contact':contact ,'location':location ,'comp':comp})   

        

    return render(request, 'login/profile3.html', {})
   

def mechanic_view(request):
    if request.method == "POST":
        date_time = datetime.datetime.now()
        varr = request.POST
        variablee = "lllllllllllllllllllllllllllllllllllllllllllll"
        print "ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo", varr
        
        data_update = UserMachanicalComplaint(user=request.user, complaint=varr["complaint"], location=varr["location"],bulding_name=varr["bulding_name"],room_number=varr["room_number"], Mobile_number=varr["mobile_number"],pub_date=date_time,status = True )
        wifi_work_data()
        message = "Congradulations !!!!your complete has been recieved after 2 days specific Mechanicworker coming to your exact location"
        from_email = settings.EMAIL_HOST_USER
        to_email = [request.user.email]
        subject = "from djnago"
        email = EmailMessage(subject,message,from_email,to_email)
        email.send()
        message= "Congradulations!!! Your complaint has been submitted"
        return render(request, 'login/profile4.html', {'msg':message})

    return render(request, 'login/profile4.html', {"data":data_update.location})
   
   
def other_view(request):
    if request.method == "POST":
        date_time = datetime.datetime.now()
        varr = request.POST
        variablee = "lllllllllllllllllllllllllllllllllllllllllllll"
        print "ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo", varr
        
        data_update = UserOtherComplaint(user=request.user, complaint=varr["complaint"], location=varr["location"],bulding_name=varr["bulding_name"],room_number=varr["room_number"], Mobile_number=varr["mobile_number"],pub_date=date_time,status = True )
        data_update.save()
        other_work_data()
        message = "Congradulations !!!!your complete has been recieved after 2 days specific worker coming to your exact location"
        from_email = settings.EMAIL_HOST_USER
        to_email = [request.user.email]
        subject = "from djnago"
        email = EmailMessage(subject,message,from_email,to_email)
        email.send()
        data=OtherComplaintDetails.objects.all()
        userr= data[len(data) - 1].user
        worker= data[len(data) - 1].worker_name
        contact= data[len(data) - 1].worker_Mobile_number
        location= data[len(data) - 1].user_location
        comp=data[len(data) - 1].user_complaint
        return render(request, 'login/other.html', {'user':userr, 'worker':worker ,'contact':contact ,'location':location ,'comp':comp})   

        #return render(request, 'login/wifi.html', {'user':userr, 'worker':worker ,'contact':contact ,'location':location ,'comp':comp})   

        

    return render(request, 'login/profile5.html', {})


        
def wifi_worker_view(request):
    if request.method == "POST":
        date_time = datetime.datetime.now()
        
        varr = request.POST
        variablee = " "
        print " ", varr
        data = UserWifiComplaint.objects.all()
        

        admin1 = "admin1"
        data_update = WifiComplaintWorker(first_name=varr["first_name"], middle_name=varr["middle_name"], last_name=varr["last_name"], Mobile_number=varr["mobile_number"],email=varr["email"], pub_date=date_time )
        data_update.save()
        authuser = User(first_name=varr["first_name"],last_name=varr["last_name"], username=varr["mobile_number"],password="admin1")
        authuser.save()
        users = User.objects.get(username=varr["mobile_number"])
        users.set_password(users.password)
        users.save()
        print data_update
        message= "Congradulations!!! Your registration has been submitted"
        return render(request, 'login/wifiworker.html', {'msg':message})
    msgg="Welcome!!! Please Register Here"
    return render(request, 'login/wifiworker.html', {'msg':msgg})

def civil_worker_view(request):
    if request.method == "POST":
        date_time = datetime.datetime.now()
        varr = request.POST
        variablee = " "
        print " ", varr
        
        data_update = CivilComplaintWorker(first_name=varr["first_name"], middle_name=varr["middle_name"],last_name=varr["last_name"], Mobile_number=varr["mobile_number"],email=varr["email"] ,pub_date=date_time )
        data_update.save()
        authuser = User(first_name=varr["first_name"],last_name=varr["last_name"], username=varr["mobile_number"],password="admin1")
        authuser.save()
        users = User.objects.get(username=varr["mobile_number"])
        users.set_password(users.password)
        users.save()
        print data_update
        message= "Congradulations!!! Your registration has been submitted"
        return render(request, 'login/civilworker.html', {'msg':message})
    msgg="Welcome!!! Please Register Here"
    return render(request, 'login/civilworker.html', {'msg':msgg})

def electric_worker_view(request):
    if request.method == "POST":
        date_time = datetime.datetime.now()
        varr = request.POST
        variablee = " "
        print " ", varr
        
        data_update = ElectricComplaintWorker(first_name=varr["first_name"], middle_name=varr["middle_name"], last_name=varr["last_name"], Mobile_number=varr["mobile_number"],email=varr["email"],pub_date=date_time )
        data_update.save()
        authuser = User(first_name=varr["first_name"],last_name=varr["last_name"], username=varr["mobile_number"],password="admin1")
        authuser.save()
        users = User.objects.get(username=varr["mobile_number"])
        users.set_password(users.password)
        users.save()
        print data_update
        message= "Congradulations!!! Your registration has been submitted"
        return render(request, 'login/electricworker.html', {'msg':message})
    msgg="Welcome!!! Please Register Here"
    return render(request, 'login/electricworker.html', {'msg':msgg})


def other_worker_view(request):
    if request.method == "POST":
        date_time = datetime.datetime.now()
        varr = request.POST
        variablee = " "
        print " ", varr
        
        data_update = OtherComplaintWorker(first_name=varr["first_name"], middle_name=varr["middle_name"], last_name=varr["last_name"], Mobile_number=varr["mobile_number"], email=varr["email"],pub_date=date_time )
        data_update.save()
        authuser = User(first_name=varr["first_name"],last_name=varr["last_name"], username=varr["mobile_number"],password="admin1")
        authuser.save()
        users = User.objects.get(username=varr["mobile_number"])
        users.set_password(users.password)
        users.save()
        print data_update
        message= "Congradulations!!! Your registration has been submitted"
        return render(request, 'login/otherworker.html', {'msg':message})
    msgg="Welcome!!! Please Register Here"
    return render(request, 'login/otherworker.html', {'msg':msgg})






def wifi_work_data():
    date_time = datetime.datetime.now()
    model=WifiComplaintWorker
    data=UserWifiComplaint.objects.all()
    #data=UserWifiComplaint.objects.filter(status = False)
    data1=WifiComplaintWorker.objects.all()
    var1=len(data1)  
    k=0  
    for i in data:
        data_up = WifiComplaintDetails(user=i.user,user_complaint=i.complaint,user_location=i.location,user_Mobile_number=i.Mobile_number,worker_name=data1[k].first_name,worker_Mobile_number=data1[k].Mobile_number,email=i.email,pub_date=date_time)
        data_up.save()
        k= (k+1)%var1
    print data_up.user
    print data_up.worker_name
        
    #return render('login/wifi.html', {'user':data_up.user, 'worker':data_up.worker_name})   
        
        

def civil_work_data(request):
    date_time = datetime.datetime.now()
    model=CivilComplaintWorker
    data=UserCivilComplaint.objects.all()
    data1=CivilComplaintWorker.objects.all()
    
    var1=len(data1)  
    k=0  
    for i in data:
        data_up = CivilComplaintDetails(user=i.user,user_complaint=i.complaint,user_location=i.location,user_Mobile_number=i.Mobile_number,worker_name=data1[k].first_name,worker_Mobile_number=data1[k].Mobile_number,pub_date=date_time)
        data_up.save()
        k= (k+1)%var1
    print data_up.user
    print data_up.worker_name
    
    

def electric_work_data(request):
    date_time = datetime.datetime.now()
    model=ElectricComplaintWorker
    data=UserElectricComplaint.objects.all()
    data1=ElectricComplaintWorker.objects.all()
    

    var1=len(data1)  
    k=0  
    for i in data:
        data_up = ElectricComplaintDetails(user=i.user,user_complaint=i.complaint,user_location=i.location,user_Mobile_number=i.Mobile_number,worker_name=data1[k].first_name,worker_Mobile_number=data1[k].Mobile_number,pub_date=date_time)
        data_up.save()
        k= (k+1)%var1
    print data_up.user
    print data_up.worker_name
    msgg="hello"
    return render(request, 'login/electric_data.html', {'msg':msgg})


def other_work_data():
    date_time = datetime.datetime.now()
    model=OtherComplaintWorker
    data=UserOtherComplaint.objects.all()
    data1=OtherComplaintWorker.objects.all()
    

    var1=len(data1)  
    k=0  
    for i in data:
        data_up = OtherComplaintDetails(user=i.user,user_complaint=i.complaint,user_location=i.location,user_Mobile_number=i.Mobile_number,worker_name=data1[k].first_name,worker_Mobile_number=data1[k].Mobile_number,pub_date=date_time)
        data_up.save()
        k= (k+1)%var1
    

    
def admin_wifi_data(request):
    data=WifiComplaintDetails.objects.all()
    return render(request, 'login/admin_wifi_data.html', {'data':data})


def admin_civil_data(request):
    data=CivilComplaintDetails.objects.all()
    return render(request, 'login/admin_civil_data.html', {'data':data})

def admin_electric_data(request):
    data=ElectricComplaintDetails.objects.all()
    return render(request, 'login/admin_electric_data.html', {'data':data})


def admin_other_data(request):
    data=OtherComplaintDetails.objects.all()
    return render(request, 'login/admin_other_data.html', {'data':data})


def wifi_worker_inp(request):
    data=WifiComplaintDetails.objects.all()
    complaints = WifiComplaintDetails.objects.filter(worker_Mobile_number=request.user.username,status=False).order_by('-id')
    if request.method == "POST":
        date_time = datetime.datetime.now()
        varr = request.POST
        variablee = "llllllll"
        print " ", varr
        print request.user.username
        var1=int(varr["id"])
        print var1
        
    
        k=[]
        for i in complaints:
            k.append(i.id)
        if var1 in k:
            #com = WifiComplaintDetails.objects.get(id=var1)
            WifiComplaintDetails.objects.filter(id=var1).update(status=True)
            con=WifiComplaintDetails.objects.filter(id=var1)
            print con[0].email
            var12 =str(con[0].user)
            var10= str(con[0].worker_name)
            var11=str(con[0].email)
            message = "Hello " + var12 + " Congradulations !!!! your complaint has been completed by Mr. " +var10+ "  Successfully.And if any query in this service then please contact to (admin123@gmail.com)  admin side"
            from_email = settings.EMAIL_HOST_USER
            to_email = [con[0].email]
            subject = "from djnago"
            email = EmailMessage(subject,message,from_email,to_email)
            email.send()
            
            
        else:
            print "No"
    for complaint in complaints:
        print "workername",complaint.id,complaint.user,complaint.user_location,complaint.user_Mobile_number,complaint.user_complaint,complaint.status
        return render(request, 'login/w.html',{'comp':complaints}) 
    
    return render(request, "login/w.html", {})

def wifi_worker_complete_status(request):
    complaints = WifiComplaintDetails.objects.filter(worker_Mobile_number=request.user.username,status=True).order_by('-id')
    for complaint in complaints:
        print "workername",complaint.id,complaint.user,complaint.user_location,complaint.user_Mobile_number,complaint.user_complaint,complaint.status
        return render(request, 'login/complete_status.html',{'comp':complaints}) 
    
    return render(request, "login/complete_status.html", {})
    
def user_status_wifi_completed(request):
    data1=WifiComplaintDetails.objects.filter(user=request.user,status=True)
    for i in data1:
        return render(request, 'login/completed_status.html',{'dt':data1}) 
    return render(request, 'login/completed_status.html',{'dt':data1}) 
    
def user_status_wifi_inprogress(request):
    data2=WifiComplaintDetails.objects.filter(user=request.user,status=False)
    for j in data2:
        return render(request, 'login/inpro.html',{'dt':data2}) 
def user_status_civil_inprogress(request):
    data2=CivilComplaintDetails.objects.filter(user=request.user,status=False)
    for j in data2:
        return render(request, 'login/civil_inpro_status.html',{'dt':data2}) 
    return render(request, 'login/empty.html',{'dt':data2}) 
def user_status_civil_completed(request):
    data2=CivilComplaintDetails.objects.filter(user=request.user,status=True)
    for j in data2:
        return render(request, 'login/civil_comp_status.html',{'dt':data2}) 
def user_status_electric_inprogress(request):
    data2=ElectricComplaintDetails.objects.filter(user=request.user,status=False)
    for j in data2:
        return render(request, 'login/electric_inpro_status.html',{'dt':data2}) 
def user_status_electric_completed(request):
    data2=ElectricComplaintDetails.objects.filter(user=request.user,status=True)
    for j in data2:
        return render(request, 'login/electric_comp_status.html',{'dt':data2}) 

def user_status_other_inprogress(request):
    data2=OtherComplaintDetails.objects.filter(user=request.user,status=False)
    for j in data2:
        return render(request, 'login/other_inpro_status.html',{'dt':data2}) 
def user_status_other_completed(request):
    data2=OtherComplaintDetails.objects.filter(user=request.user,status=True)
    for j in data2:
        return render(request, 'login/other_comp_status.html',{'dt':data2}) 

def civil_worker_inp(request):
    data=CivilComplaintDetails.objects.all()
    complaints = CivilComplaintDetails.objects.filter(worker_Mobile_number=request.user.username,status=False)
    if request.method == "POST":
        date_time = datetime.datetime.now()
        varr = request.POST
        variablee = "llllllll"
        print " ", varr
        print request.user.username
        var1=int(varr["id"])
        print var1
        
    
        k=[]
        for i in complaints:
            k.append(i.id)
        if var1 in k:
            #com = WifiComplaintDetails.objects.get(id=var1)
            CivilComplaintDetails.objects.filter(id=var1).update(status=True)
            con=CivilComplaintDetails.objects.filter(id=var1)
            print con[0].email
            message = "Congradulations !!!!your completed"
            from_email = settings.EMAIL_HOST_USER
            to_email = [con[0].email]
            subject = "from djnago"
            email = EmailMessage(subject,message,from_email,to_email)
            email.send()
            
            
        else:
            print "No"
    for complaint in complaints:
        print "workername",complaint.id,complaint.user,complaint.user_location,complaint.user_Mobile_number,complaint.user_complaint,complaint.status
        return render(request, 'login/c.html',{'comp':complaints}) 
    
    return render(request, "login/c.html", {})

def civil_worker_complete_status(request):
    complaints = CivilComplaintDetails.objects.filter(worker_Mobile_number=request.user.username,status=True)
    for complaint in complaints:
        print "workername",complaint.id,complaint.user,complaint.user_location,complaint.user_Mobile_number,complaint.user_complaint,complaint.status
        return render(request, 'login/cc.html',{'comp':complaints}) 
    
    return render(request, "login/cc.html", {})

def electric_worker_inp(request):
    data=ElectricComplaintDetails.objects.all()
    complaints = ElectricComplaintDetails.objects.filter(worker_Mobile_number=request.user.username,status=False)
    if request.method == "POST":
        date_time = datetime.datetime.now()
        varr = request.POST
        variablee = "llllllll"
        print " ", varr
        print request.user.username
        var1=int(varr["id"])
        print var1
        
    
        k=[]
        for i in complaints:
            k.append(i.id)
        if var1 in k:
            #com = WifiComplaintDetails.objects.get(id=var1)
            ElectricComplaintDetails.objects.filter(id=var1).update(status=True)
            con=ElectricComplaintDetails.objects.filter(id=var1)
            print con[0].email
            message = "Congradulations !!!!your completed"
            from_email = settings.EMAIL_HOST_USER
            to_email = [con[0].email]
            subject = "from djnago"
            email = EmailMessage(subject,message,from_email,to_email)
            email.send()
            
            
        else:
            print "No"
    for complaint in complaints:
        print "workername",complaint.id,complaint.user,complaint.user_location,complaint.user_Mobile_number,complaint.user_complaint,complaint.status
        return render(request, 'login/e.html',{'comp':complaints}) 
    
    return render(request, "login/e.html", {})

def electric_worker_complete_status(request):
    complaints = ElectricComplaintDetails.objects.filter(worker_Mobile_number=request.user.username,status=True)
    for complaint in complaints:
        print "workername",complaint.id,complaint.user,complaint.user_location,complaint.user_Mobile_number,complaint.user_complaint,complaint.status
        return render(request, 'login/ec.html',{'comp':complaints}) 
    
    return render(request, "login/ec.html", {})

def other_worker_inp(request):
    data=OtherComplaintDetails.objects.all()
    complaints = OtherComplaintDetails.objects.filter(worker_Mobile_number=request.user.username,status=False)
    if request.method == "POST":
        date_time = datetime.datetime.now()
        varr = request.POST
        variablee = "llllllll"
        print " ", varr
        print request.user.username
        var1=int(varr["id"])
        print var1
        
    
        k=[]
        for i in complaints:
            k.append(i.id)
        if var1 in k:
            #com = WifiComplaintDetails.objects.get(id=var1)
            OtherComplaintDetails.objects.filter(id=var1).update(status=True)
            con=OtherComplaintDetails.objects.filter(id=var1)
            print con[0].email
            message = "Congradulations !!!!your completed"
            from_email = settings.EMAIL_HOST_USER
            to_email = [con[0].email]
            subject = "from djnago"
            email = EmailMessage(subject,message,from_email,to_email)
            email.send()
            
            
        else:
            print "No"
    for complaint in complaints:
        print "workername",complaint.id,complaint.user,complaint.user_location,complaint.user_Mobile_number,complaint.user_complaint,complaint.status
        return render(request, 'login/o.html',{'comp':complaints}) 
    
    return render(request, "login/o.html", {})

def other_worker_complete_status(request):
    complaints = OtherComplaintDetails.objects.filter(worker_Mobile_number=request.user.username,status=True)
    for complaint in complaints:
        print "workername",complaint.id,complaint.user,complaint.user_location,complaint.user_Mobile_number,complaint.user_complaint,complaint.status
        return render(request, 'login/oc.html',{'comp':complaints}) 
    
    return render(request, "login/oc.html", {})

