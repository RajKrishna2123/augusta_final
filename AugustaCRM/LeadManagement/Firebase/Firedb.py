import pyrebase
from datetime import datetime

import os

FIREBASE_CONFIG = {
    'apiKey': str(os.getenv('FIREBASE_API_KEY')),
    'authDomain': str(os.getenv('FIREBASE_AUTH_DOMAIN')),
    'databaseURL': "https://augusta-crm-95afd-default-rtdb.asia-southeast1.firebasedatabase.app/",
    'projectId': str(os.getenv('FIREBASE_PROJECT_ID')),
    'storageBucket': str(os.getenv('FIREBASE_STORAGE_BUCKET')),
    'messagingSenderId': str(os.getenv('FIREBASE_MESSAGING_SENDER_ID')),
    'appId': str(os.getenv('FIREBASE_APP_ID')),
    'measurementId': str(os.getenv('FIREBASE_MEASUREMENT_ID')),
}

firebase = pyrebase.initialize_app(FIREBASE_CONFIG)
auth_fb = firebase.auth()
db = firebase.database()


def newleadlist():
    result = db.child("New Leads").get()
    result = result.val()
    i = 0
    rec={}
    for key, value in result.items():
        # print(f"Key: {key}")
        dic1 = {}
        for sub_key, sub_value in value.items():

            dic2= {sub_key:sub_value}
            dic1 = dic1 | dic2
            rec[i]= dic1
        i = i+1
    return rec

def move_to_call_list():
    result = db.child("New Leads").get()
    result = result.val()
    i = 0
    rec={}
    for key, value in result.items():
        # print(f"Key: {key}")
        dic1 = {}
        for sub_key, sub_value in value.items():

            dic2= {sub_key:sub_value}
            dic1 = dic1 | dic2
            rec[i]= dic1
        i = i+1
    record = rec[0]
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = {"Attempted":now,"status": "pending", "Attempt_no":1}
    record = record | data
    db.child("Call List").push(record)
    rkey = ""
    for key, value in result.items():
        rkey = key
        break
    db.child("New Leads").child(rkey).remove()


def get_Call_List():
    result = db.child("Call List").get()
    result = result.val()
    i = 0
    rec={}
    for key, value in result.items():
        
        dic1 = {}
        for sub_key, sub_value in value.items():

            dic2= {sub_key:sub_value}
            dic1 = dic1 | dic2
            rec[i]= dic1
        i = i+1
    return rec
