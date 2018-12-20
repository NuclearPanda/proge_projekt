import speech_recognition as sr
from tkinter import *
from tkinter import ttk
from random import randint
import time
from cleverwrap import CleverWrap


class speak:
    def __init__(self, google_apikey, cleverbot_apikey):
        self.cleverbot_apikey = cleverbot_apikey
        self.google_apikey = google_apikey # apikey failinimi
        self.gui = Tk() # tkinteri init
        self.record_btn_text = StringVar()
        self.wait_var = IntVar()
        self.running = True

    def Main(self):
        self.gui.title("Action")
        self.gui.geometry("500x500")
        self.wait_var = IntVar()
        start_btn = ttk.Button(self.gui, text="Start", command=lambda: self.wait_var.set(1))
        start_btn.grid(row=0,ipadx=210)
        exit_button = ttk.Button(self.gui, text='Exit', command=self.shutdown)
        exit_button.grid(row=1,column=0,ipadx=210)
        start_btn.wait_variable(self.wait_var) # ootab et start nuppu vajutataks
        empty_line = Label(self.gui, text='') # tühi rida vahele
        empty_line.grid(row=2)
        speech_array = []
        while self.running: # mainloop() asenduseks et GUI püsiks
            self.record_btn_text.set('Start listening')
            record_btn = ttk.Button(self.gui, textvariable=self.record_btn_text, command=self.wait)
            record_btn.grid(row=0, ipadx=210)
            record_btn.wait_variable(self.wait_var)
            if self.running:
                speech = self.recognize()
            else:
                exit(0)
            if speech == 'exit ':
                exit(0)
            response = self.cleverbot(speech)
            if speech is None:
                continue
            speech = 'You: ' + speech
            response = 'Cleverbot: ' + response
            speech_array.append(Label(self.gui, text=speech))
            speech_array.append(Label(self.gui, text=response))
            if len(speech_array)>20:
                speech_array.pop(0).destroy()
                speech_array.pop(0).destroy()
            for i in range(3,len(speech_array)+3):
                speech_array[i-3].grid(row=i)
            self.gui.update_idletasks()
            self.gui.update()


    def recognize(self):
        # aktiveerib mikrofoni ja kuulab kuni on vaikus
        r = sr.Recognizer()
        r.dynamic_energy_threshold = True
        with sr.Microphone() as source:
            print('Started listening.')
            audio = r.listen(source, phrase_time_limit=5)
        print("Stopped listening.")
        self.record_btn_text.set('Stopped listening')
        self.gui.update()

        try:
            credentials = open(self.google_apikey).read()
        except FileNotFoundError:
            print(self.google_apikey, 'file not found')
            exit(1)
        try:
            speech_to_text = r.recognize_google_cloud(audio, credentials_json=credentials)
        except sr.UnknownValueError:
            print("Google Cloud Speech could not understand audio")
            return None
        except sr.RequestError as e:
            print("Could not request results from Google Cloud Speech service; {0}".format(e))
            raise FileNotFoundError
        return speech_to_text

    def cleverbot(self,speech):
        self.record_btn_text.set('Waiting for cleverbot response...')
        self.gui.update()
        try:
            self.cw = CleverWrap(open(self.cleverbot_apikey).read())
        except FileNotFoundError:
            print(self.cleverbot_apikey, 'file was not found')
            raise FileNotFoundError
        vastus = self.cw.say(speech)
        return vastus

    def wait(self):
        self.record_btn_text.set('Listening now')
        self.wait_var.set(1)
        self.gui.update()

    def shutdown(self):
        self.running = False
        self.cw.reset()
        self.wait_var.set(2)


test = speak('apikey.json', 'cleverbotkey.txt')
test.Main()