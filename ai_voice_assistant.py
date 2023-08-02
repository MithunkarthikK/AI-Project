import tkinter
import speech_recognition as sr
import datetime
import wikipedia
import os
import shutil
import pyttsx3
import subprocess
import json
import pyjokes
import pyaudio

import webbrowser
from urllib.request import urlopen

engine=pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)

    if hour>=5 and hour<12:
        speak("Good morning baby..!")
    elif hour>=12 and hour<17:
        speak("Good afternoon baby..!")
    elif hour>=17 and hour<20:
        speak("Good evening baby..!")
    else:
        speak("Good night sweat dream sugar..!")
    
    asname=("hinata hyuga")
    speak("Im your baby")
    speak(asname)
def user():
    speak("what can i call you baby")
    username=takecmd()
    speak(username)
    speak("what you need baby tell me anything i can do anything for you baby",username)

def takecmd():
    r= sr.Recognizer() 
    with  sr.Microphone() as source:
        print("I'm hearing..")
        speak("I'm hearing..")
        r.pause_threshold =1
        audio = r.listen(source)
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language ='en-in,tamil-in')
        print(f"User said: {query}\n")
  
    except Exception as e:
        print(e)   
        print("Unable to Recognize your voice.") 
        return "None"
     
    return query

# fun call
if __name__=='__main__':
    clear = lambda:os.system('cls')

    clear()
    wishMe()
    user()

    while True:
        query = takecmd().lower()

        if "wikipedia" in query:
            speak("can you wait for a seconds baby..PLEASE!")
            query=query.replace("wikipedia", "")
            result=wikipedia.summary(query,sentences = 3)
            speak("baby in wiki i found this..baby")
            print(result)
            speak(result,"can you get it baby..!")
        
        elif "open google" in query:
            speak("here you go baby..!")
            webbrowser.open("www.google.com")

        elif "open youtube " in query:
            speak("here you go baby..!")
            webbrowser.open("www.youtube.com") 

        elif "can you tell me a joke" in query:
            speak("oh yeah baby...are you like me that much")
            speak(pyjokes.get_joke())
        
        elif "hinata huyga" in query:
             
            wishMe()
            speak("naruto kun")
            speak("Aishitemasu")
        
        elif "i love you" in query:
            speak("Aishitemasu naruto kun..")

