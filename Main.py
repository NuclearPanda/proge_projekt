import speech_recognition as sr
from tkinter import *
from tkinter import ttk
from random import randint


class speak:
    def __init__(self,apikey):
        self.apikey = apikey # apikey failinimi
        self.gui = Tk() # tkinteri init
    def Main(self):
        self.gui.title("Action")
        self.gui.geometry("500x500")
        wait = IntVar()
        start_btn = ttk.Button(self.gui, text="Start", command=lambda: wait.set(1))
        start_btn.grid(row=0,ipadx=210)
        exit_label = Label(self.gui, text='Say exit to exit')
        exit_label.grid(row=1,column=0,ipadx=210)
        start_btn.wait_variable(wait) # ootab et start nuppu vajutataks
        empty_line = Label(self.gui, text='') # tühi rida vahele
        empty_line.grid(row=2)
        speech_array = []
        while True: # mainloop() asenduseks et GUI püsiks
            speech = self.recognize()
            #respone = self.cleverbot(speech)
            response = 'Cleverbot vastus'
            #speech = str(randint(0,9)) #testimiseks, kui ei saa rääkida
            if speech == 'exit ':
                exit(0)
            if speech is None:
                continue
            speech = 'You: ' + speech
            #response = 'Cleverbot: ' + response
            speech_array.append(Label(self.gui, text=speech))
            speech_array.append(Label(self.gui, text=response))
            if len(speech_array)>20:
                speech_array.pop(0).destroy()
                speech_array.pop(0).destroy()
            for i in range(3,len(speech_array)+3):
                speech_array[i-3].grid(row=i)
                print(i)
            self.gui.update_idletasks()
            self.gui.update()


    def recognize(self):
        # aktiveerib mikrofoni ja kuulab kuni on vaikus
        r = sr.Recognizer()
        r.dynamic_energy_threshold = True
        with sr.Microphone() as source:
            print('Started listening.')
            audio = r.listen(source, phrase_time_limit=3)
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

    def cleverbot(self,speech):
        pass



test = speak('apikey.json')
test.Main()