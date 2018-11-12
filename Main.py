import speech_recognition as sr
from tkinter import *
from tkinter import ttk


def start_button():
    start_btn_frame = Tk()
    start_btn_frame.title("Action")
    start_btn_frame.geometry("300x100")

    # loome nupu
    start_btn = ttk.Button(start_btn_frame, text="Record", command=start_btn_frame.destroy)
    start_btn.place(x=70, y=40, width=150)

    # ilmutame akna ekraanile
    start_btn_frame.mainloop()

def listening_msgbox():
    #ToDo Aken, mis asendab printi

    print("Listening! Please speak")

def answer_to_GUI(you_said):
    answer_frame = Tk()
    answer_frame.title("To Cleverbot")
    answer_frame.geometry("300x100")
    answer_label = ttk.Label(answer_frame,
                             text="You said -" + you_said)
    answer_label.place(x=100, y=20)
    answer_frame.mainloop()


# aktiveerib mikrofoni ja kuulab kuni on vaikus
r = sr.Recognizer()
with sr.Microphone() as source:
    start_button()
    listening_msgbox()
    audio = r.listen(source)
print("Stopped listening.")

filename = input('Sisesta API key json faili nimi: ')
credentials = open(filename).read()

try:
    speech_to_text = r.recognize_google_cloud(audio, credentials_json=credentials)
    answer_to_GUI(speech_to_text)
    # print("You said: " + r.recognize_google_cloud(audio, credentials_json=credentials))
except sr.UnknownValueError:
    print("Google Cloud Speech could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Cloud Speech service; {0}".format(e))
