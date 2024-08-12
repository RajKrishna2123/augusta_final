# Create your views here.
import json
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib import auth
import pyrebase
from datetime import datetime
from .serializer import DataSerializer
from rest_framework.renderers import JSONRenderer
from .Firebase.Firedb import *



import os

''' FIREBASE_CONFIG = {
    'apiKey': str(os.getenv('FIREBASE_API_KEY')),
    'authDomain': str(os.getenv('FIREBASE_AUTH_DOMAIN')),
    'databaseURL': str(os.getenv('FIREBASE_DATABASE_URL')),
    'projectId': str(os.getenv('FIREBASE_PROJECT_ID')),
    'storageBucket': str(os.getenv('FIREBASE_STORAGE_BUCKET')),
    'messagingSenderId': str(os.getenv('FIREBASE_MESSAGING_SENDER_ID')),
    'appId': str(os.getenv('FIREBASE_APP_ID')),
    
} '''
FIREBASE_CONFIG = {
    'apiKey': 'AIzaSyC1TfBBNAsC7IBP32ES24IQs2AAqm4zVwM',
    'authDomain': 'augusta-crm-95afd.firebaseapp.com',
    'databaseURL': 'https://augusta-crm-95afd-default-rtdb.asia-southeast1.firebasedatabase.app/',
    'projectId': 'augusta-crm-95afd',
    'storageBucket': 'augusta-crm-95afd.appspot.com',
    'messagingSenderId': '166508227104',
    'appId': '1:166508227104:web:da21808b6c8b55ac49ea45',
    'measurementId': 'G-0TRE4F4Z6Q',
}
print(FIREBASE_CONFIG)
firebase = pyrebase.initialize_app(FIREBASE_CONFIG)
auth_fb = firebase.auth()
db = firebase.database()
rec_num=0
new_rec_num=0
def index(request):
    return render(request, "index.html",{"next_action":"services/"})

def services(request):
    rec_num=0
    new_rec_num=0
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
def EmptyNewLeads(request):
    return render(request,"EmptyNewLeads.html")

def EmptyCallList(request):
    return render(request,"EmptyCall-List.html")


def CallLeads(request):
    return render(request, "call-leads.html")

def NewLeads(request):
    try:
        rec = newleadlist()
        if not rec:
            return redirect('/empty-newlead')
    
    
        
        point = rec[new_rec_num]
        
        # point= db.child("local_test").child("lead_details").child("email").get()
        email = point["Email"]
        # point= db.child("local_test").child("lead_details").child("name").get()
        name =  point["Name"]
        # point= db.child("local_test").child("lead_details").child("name").get()
        phone = point["phone"]
        # point= db.child("local_test").child("lead_details").child("name").get()
        time = point["Created"]
        # point= db.child("local_test").child("lead_details").child("name").get()
        source = point["Platform"]
        return render(request, "new-leads.html", {"email": email, "name": name, "phone": phone, "time": time, "source": source})
    except:
        redirect('/empty-newleads')
def Newcalendly(request):
    new_rec_num = 0
    move_to_archive("booked")
    return render(request, "calendly.html")

def NewCallBack(request):
    new_rec_num=new_rec_num + 1
    move_to_call_list("call back later")
    return redirect('services/call-leads/new-leads')

def NewNotAnswred(request):
    new_rec_num=new_rec_num + 1
    move_to_call_list("Not Answred")
    return redirect('services/call-leads/new-leads')

def NewNotIntrested(request):
    new_rec_num = 0
    move_to_archive("Not intrested")
    return redirect('services/call-leads/new-leads')

def NewInvalid(request):
    move_to_archive("Invalid phone number")
    new_rec_num = 0

    return redirect('services/call-leads/new-leads')

def CallList(request):
    try:
        rec = get_Call_List()
        point = rec[rec_num]
    
        email = point["Email"]
        name =  point["Name"]
        phone = point["phone"]
        time = point["Created"]
        source = point["Platform"]
        
        return render(request, "call-list.html", {"email": email, "name": name, "phone": phone, "time": time, "source": source})
    except:
        redirect('/empty-call-list')

def CallResult(request):
    
    return render(request, "call-result.html")

def Call(request):    
    return redirect("/")


def calendly(request):
    rec_num=0
    result = db.child("Call List").get()
    result = result.val()
    rkey=""
    rec = get_Call_List()
    point = rec[0]
    attempt_no = point["Attempt_no"]
    # phone = point["phone"]
    for key, value in result.items():
        rkey = key
        break
    attempt_no = attempt_no +1
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    db.child("Call List").child(rkey).update({"Attempt_no": attempt_no})
    db.child("Call List").child(rkey).update({"Attempted": now})
    db.child("Call List").child(rkey).update({"status": "Booked"})
    db.child("Archived").push(point)
    db.child("Call List").child(rkey).remove()

    return render(request, "calendly.html")


def ResultLog(request):
    return render(request, "result-log.html")

def CallBackLater(request):
    rec_num = rec_num +1
    result = db.child("Call List").get()
    result = result.val()
    rkey=""
    rec = get_Call_List()
    point = rec[0]
    attempt_no = point["Attempt_no"]
    # phone = point["phone"]
    for key, value in result.items():
        rkey = key
        break
    attempt_no = attempt_no +1
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    db.child("Call List").child(rkey).update({"Attempt_no": attempt_no})
    db.child("Call List").child(rkey).update({"Attempted": now})
    db.child("Call List").child(rkey).update({"status": "Call back later"})
    num = point["Attempt_no"]
    if num >= 10:
        db.child("Archived").push(point)
        db.child("Call List").child(rkey).remove()

    return redirect('/services/call-leads/Call-list')

def NotAnswered(request):
    #Crud operation code
    rec_num = rec_num +1
    result = db.child("Call List").get()
    result = result.val()
    rkey=""
    rec = get_Call_List()
    point = rec[0]
    attempt_no = point["Attempt_no"]
    # phone = point["phone"]
    for key, value in result.items():
        rkey = key
        break
    attempt_no = attempt_no +1
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    db.child("Call List").child(rkey).update({"Attempt_no": attempt_no})
    db.child("Call List").child(rkey).update({"Attempted": now})
    db.child("Call List").child(rkey).update({"status": "Not answred"})
    num = point["Attempt_no"]
    if num >= 10:
        db.child("Archived").push(point)
        db.child("Call List").child(rkey).remove()

    return redirect('/services/call-leads/Call-list')
    

def NotIntrested(request):
    result = db.child("Call List").get()
    result = result.val()
    rkey=""
    rec = get_Call_List()
    point = rec[0]
    attempt_no = point["Attempt_no"]
    # phone = point["phone"]
    for key, value in result.items():
        rkey = key
        break
    attempt_no = attempt_no +1
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    db.child("Call List").child(rkey).update({"Attempt_no": attempt_no})
    db.child("Call List").child(rkey).update({"Attempted": now})
    db.child("Call List").child(rkey).update({"status": "Not Intrested"})
    db.child("Archived").push(point)
    db.child("Call List").child(rkey).remove()    
    return redirect('/services/call-leads/call-list')

def Invalid(request):
    result = db.child("Call List").get()
    result = result.val()
    rkey=""
    rec = get_Call_List()
    point = rec[0]
    attempt_no = point["Attempt_no"]
    # phone = point["phone"]
    for key, value in result.items():
        rkey = key
        break
    attempt_no = attempt_no +1
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    db.child("Call List").child(rkey).update({"Attempt_no": attempt_no})
    db.child("Call List").child(rkey).update({"Attempted": now})
    db.child("Call List").child(rkey).update({"status": "Invalid phone number"})
    db.child("Archived").push(point)
    db.child("Call List").child(rkey).remove()    
    return redirect('/services/call-leads/call-list')
