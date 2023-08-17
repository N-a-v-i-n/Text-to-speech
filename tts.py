import tkinter, pyttsx3
from tkinter import *
from tkinter import ttk, messagebox
import os, time


class Tts():
    def speak(self): 
        request_voice=select_voice.get()
        request_rate=speed_select.get()
        speech=pyttsx3.init()
        
        voice=speech.getProperty('voices')
        if request_voice == "female":
            speech.setProperty('voice',voice[1].id)
        else:
            speech.setProperty('voice',voice[0].id)

        speech.setProperty("rate",request_rate)
        get_text=input_data.get("1.0",'end-1c')
        speech.say(get_text)
        self.speech=speech
        speech.runAndWait()

    def download(self):
        print("Pressed")
        request_voice=select_voice.get()
        request_rate=speed_select.get()
        speech=pyttsx3.init()
        voice=speech.getProperty('voices')
        if request_voice == "female":
            speech.setProperty('voice',voice[1].id)
        else:
            speech.setProperty('voice',voice[0].id)

        speech.setProperty("rate",request_rate)
        get_text=input_data.get("1.0",'end-1c')
        print("get _words : ",get_text)
        if get_text != "" :
            do_save=speech.save_to_file(get_text, f"Audio_{time.time()}.mp3")
        else:
            msg=messagebox.showinfo(title="Warning",message="NOT ALLOWED TO DOWNLOAD")

        speech.runAndWait()
    
obj1=Tts()

window = tkinter.Tk()
window.geometry("800x600")
window.title("Text to Speech")
window.resizable(0,0)
l1=Label(window,text="Text can Wirte/CopyPaste below Textarea")
l1.pack()
input_data=Text(window,width=100,height=5,font="arial,8")
input_data.pack(pady=10,padx=20)

select_voice_label=Label(window,text="Please select Voice, Default Male")
select_voice_label.pack(pady=10)
select_voice=ttk.Combobox(window,values=("male","female"))
select_voice.current(0)
select_voice.pack()
select_voice["state"]='readonly'

speed_label=Label(window,text="Speed")
speed_label.pack()
speed_select = Spinbox(window,from_=100,to=1000)
speed_select.pack(pady=10)


Speak_btn=Button(text="Speak",width=15,height=2,command=obj1.speak,bg="royalblue",fg="white")
Speak_btn.pack()



download_mp3=Button(window,text="Download",command=obj1.download)
download_mp3.pack(pady=30)























window.mainloop()