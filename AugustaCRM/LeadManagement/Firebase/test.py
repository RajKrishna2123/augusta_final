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

now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
data = {"Created":now, "Email":"rkdk23@gmail.com", "Name": "Raj", "phone": "+9156473126", "Platform": "in", "status": "pending"}
# db.child("New Leads").push(data)
# point=db.child("leads_details").child("email").get()
# # point= db.child("local_test").child("lead_details").child("email").get()
# email = point.val()
# print(email)
result = db.child("New Leads").get()
result = result.val()
# rec=result.val()
# print(rec)
# for traversing and storing values
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

print(rec[3])


# count = len(rec.keys())
# print(count)