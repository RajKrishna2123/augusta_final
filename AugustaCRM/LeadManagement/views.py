# Create your views here.
import json
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib import auth
import pyrebase
from datetime import datetime
from .serializer import DataSerializer
from rest_framework.renderers import JSONRenderer



import os

FIREBASE_CONFIG = {
    'apiKey': str(os.getenv('FIREBASE_API_KEY')),
    'authDomain': str(os.getenv('FIREBASE_AUTH_DOMAIN')),
    'databaseURL': str(os.getenv('FIREBASE_DATABASE_URL')),
    'projectId': str(os.getenv('FIREBASE_PROJECT_ID')),
    'storageBucket': str(os.getenv('FIREBASE_STORAGE_BUCKET')),
    'messagingSenderId': str(os.getenv('FIREBASE_MESSAGING_SENDER_ID')),
    'appId': str(os.getenv('FIREBASE_APP_ID')),
    'measurementId': str(os.getenv('FIREBASE_MEASUREMENT_ID')),
}
print(FIREBASE_CONFIG)
firebase = pyrebase.initialize_app(FIREBASE_CONFIG)
auth_fb = firebase.auth()
db = firebase.database()

def index(request):
    return render(request, "index.html",{"next_action":"services/"})

def services(request):
    email=request.POST.get('email')
    password=request.POST.get('password')
    try: 
        user=auth_fb.sign_in_with_email_and_password(email, password)
        session_id=user['idToken']
        request.session['uid']=str(session_id)
        return render(request, "services.html")
    except:
        if session_id:
            return render(request, "services.html")
        else:
            return render(request, "index.html", {"messages":"Invalid Credentials try again"})

def logout(request):
    auth.logout(request)
    return render(request, "index.html")

def CallLeads(request):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = {"Created":now, "Email":"rishidwd29@gmail.com", "Name": "Rishi", "phone": "+9156473126", "Platform": "fb", "status": "pending"}
    json_data = json.dumps(data)
    # serializer = DataSerializer(data=data)
    # if serializer.is_valid():
    #     json_data = JSONRenderer().render(serializer.data)
    #     print(json_data)
    
    # db.child("New Leads").push(json_data)

    # else:
    #     print(serializer.errors)
    
    point=db.child("New Leads").child("email").get()
    # point= db.child("local_test").child("lead_details").child("email").get()
    email = point.val()
    # point= db.child("local_test").child("lead_details").child("name").get()
    name = db.child("New Leads").child("name").get()
    # point= db.child("local_test").child("lead_details").child("name").get()
    phone = db.child("New Leads")
    # point= db.child("local_test").child("lead_details").child("name").get()
    time = "created at"
    # point= db.child("local_test").child("lead_details").child("name").get()
    source = "facebook"
    return render(request, "call-leads.html", {"email": email, "name": name, "phone": phone, "time": time, "source": source})

def calendly(request):
    return render(request, "calendly.html")

def ResultLog(request):
    return render(request, "result-log.html")

def CallBackLater(request):
    # Crud operation code
    return redirect('/services/call-leads/result-log')

def NotAnswered(request):
    #Crud operation code
    return redirect('/services/call-leads/result-log')

def NotIntrested(request):
    #Crud operation code
    return redirect('/services/call-leads/result-log')