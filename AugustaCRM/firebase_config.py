import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate('firebase/augusta-crm-95afd-firebase-adminsdk-phod1-9c56586087.json')
firebase_admin.initialize_app(cred)
