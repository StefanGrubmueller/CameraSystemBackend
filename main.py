import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import threading

cred = credentials.Certificate("./credentials.json")
firebase_admin.initialize_app(cred, {
  'projectId': "camera-system-frontend",
})

db = firestore.client()

bulb = db.collection(u'Jakob').document(u'Bulb')
bulbStatus =  db.collection(u'Jakob').document(u'Bulb').get().to_dict()['status']
timelapse = db.collection(u'Jakob').document(u'Timelapse')
timelapseStatus = db.collection(u'Jakob').document(u'Timelapse').get().to_dict()['status']

callback_done = threading.Event()

while True:
    if bulbStatus:
        bulb.set({'status': False})
        print('bulb active')
    elif timelapseStatus:
        timelapse.set({'status': False})
        print('timelapse active')

    