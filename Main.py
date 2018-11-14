import speech_recognition as sr
from tkinter import *
from tkinter import ttk

class speak:
    def __init__(self,apikey):
        self.apikey = apikey
        self.gui = Tk()
    def Main(self):
        self.gui.title("Action")
        self.gui.geometry("500x500")
        wait = IntVar()
        start_btn = ttk.Button(self.gui, text="Start", command=lambda: wait.set(1))
        start_btn.place(x=100, y=100, width=150)
        exit_label = Label(self.gui, text='Say exit to exit')
        exit_label.place(x=275, y=100)
        start_btn.wait_variable(wait)
        while True:
            speech = self.recognize()
            if speech == 'exit ':
                exit(0)
            if speech is None:
                continue
            speech = 'You: ' + speech
            gui_update = Label(self.gui, text=speech)
            gui_update.pack()
            self.gui.update_idletasks()
            self.gui.update()


    def recognize(self):
        # aktiveerib mikrofoni ja kuulab kuni on vaikus
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('Started listening.')
            audio = r.listen(source)
        print("Stopped listening.")

        try:
            credentials = open(self.apikey).read()
        except FileNotFoundError:
            print(self.apikey,'file not found')
            exit(1)
        try:
            speech_to_text = r.recognize_google_cloud(audio, credentials_json=credentials)
        except sr.UnknownValueError:
            print("Google Cloud Speech could not understand audio")
            return None
        except sr.RequestError as e:
            print("Could not request results from Google Cloud Speech service; {0}".format(e))
            exit(1)
        return speech_to_text



test = speak('apikey.json')
test.Main()