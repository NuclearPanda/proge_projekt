import speech_recognition as sr

# aktiveerib mikrofoni ja kuulab kuni on vaikus
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
print("Stopped listening.")


credentials = r"""{
  "type": "service_account",
  "project_id": "***REMOVED***",
  "private_key_id": "***REMOVED***",
  "private_key": "-----BEGIN PRIVATE KEY-----\n***REMOVED***\n***REMOVED***\n***REMOVED***\n***REMOVED***\***REMOVED***\n***REMOVED***\***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***\n-----END PRIVATE KEY-----\n",
  "client_email": "***REMOVED******REMOVED***.iam.gserviceaccount.com",
  "client_id": "***REMOVED***",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/sr-user%40***REMOVED***.iam.gserviceaccount.com"
}"""
try:
    print("You said: " + r.recognize_google_cloud(audio, credentials_json=credentials))
except sr.UnknownValueError:
    print("Google Cloud Speech could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Cloud Speech service; {0}".format(e))
