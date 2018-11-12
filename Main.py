import speech_recognition as sr

# aktiveerib mikrofoni ja kuulab kuni on vaikus
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
print("Stopped listening.")

filename = input('Sisesta API key json faili nimi: ')
credentials = open(filename).read()
try:
    print("You said: " + r.recognize_google_cloud(audio, credentials_json=credentials))
except sr.UnknownValueError:
    print("Google Cloud Speech could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Cloud Speech service; {0}".format(e))
