# Create your views here.
from django.shortcuts import render , redirect
from django.http import HttpResponse
import pyrebase

config = {
    'apiKey': "AIzaSyC1TfBBNAsC7IBP32ES24IQs2AAqm4zVwM",
    'authDomain': "augusta-crm-95afd.firebaseapp.com",
    'databaseURL': "https://augusta-crm-95afd-default-rtdb.asia-southeast1.firebasedatabase.app",
    'projectId': "augusta-crm-95afd",
    'storageBucket': "augusta-crm-95afd.appspot.com",
    'messagingSenderId': "166508227104",
    'appId': "1:166508227104:web:da21808b6c8b55ac49ea45",
    'measurementId': "G-0TRE4F4Z6Q"
    }
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

def index(request):
    return render(request, "index.html",{"next_action":"services/"})

def services(request):
    email=request.POST.get('email')
    password=request.POST.get('password')  
    try: 
        user=auth.sign_in_with_email_and_password(email, password)
        print(user)
        return render(request, "services.html")
    except:
        return render(request, "index.html", {"messages":"Invalid Credentials try again"})

def sign_up(request):
    return render(request, "sign-up.html")


def CallLeads(request):
    return render(request, "call-leads.html")

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