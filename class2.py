import speech_recognition as sr
import pyaudio
import socket,webbrowser
from tkinter import ttk,messagebox
import pyttsx3,datetime
import random,pyautogui,subprocess,pyjokes
from colorama import init
from colorama import Fore,Style,Back
init()
class play:
    def playing(x):
        def test():
            try:
                socket.create_connection(("google.com",80))
                return True
            except OSError:
                return False
        k=test()
        if k:
            text_speech=pyttsx3.init()
            text_speech.say("hello "+x+" say something")
            text_speech.runAndWait()
            a=sr.Recognizer()
            with sr.Microphone() as source:
                print(Fore.GREEN,"say something")
                audio=a.listen(source)
                try:
        
                    text=a.recognize_google(audio)
                    print(Fore.YELLOW,"you said: {}".format(text))
                    a=str(text).lower()
                    if str(text).lower()=="welcome":
                        print("hello "+x+" please tell something")
                    elif a=="open google":
                        webbrowser.open("www.google.com")
                    elif a=="open youtube":
                        webbrowser.open("www.youtube.com")
                    elif a=="show time" or a=="what is time now" or a=="tell time" or a=="tell current time" or a=="please tell time" or a=="time":
                        p=datetime.datetime.now()
                        print(Fore.LIGHTCYAN_EX,"Current date: ",str(p).split()[0])
                        print(Fore.LIGHTCYAN_EX,"Current time: ",str(p).split()[1])
                    elif a=="play music" or a=="play song":
                        text_speech=pyttsx3.init()
                        text_speech.say("Press b for bengali h for hindi e for english: ")
                        text_speech.runAndWait()
                        j=input("Press b for bengali h for hindi e for english: ")
                        if j.lower()=="b":
                            webbrowser.open("https://rajib3728.github.io/bengali/")
                        elif j.lower()=="h":
                            webbrowser.open("https://rajib3728.github.io/hindi/")
                        elif j.lower()=="e":
                            webbrowser.open("https://rajib3728.github.io/english/")
                        else:
                            print(Fore.RED,"wrong input 😐")
                    elif a=="jokes" or a=="say jokes" or a=="joke" or a=="say joke" or a=="tell jokes" or a=="tell joke" or a=="please tell a joke":
                        print(Fore.GREEN,"Wait! let me think")
                        b=pyjokes.get_joke()
                        text_speech=pyttsx3.init()
                        text_speech.say(b)
                        text_speech.runAndWait()
                        print(Fore.MAGENTA,Style.BRIGHT,b)
                    elif a=="open notepad" or a=="please open notepad":
                        text_speech=pyttsx3.init()
                        text_speech.say("opening notepad")
                        text_speech.runAndWait()
                        subprocess.call("notepad.exe")
                    elif a=="open calculator" or a=="please open calculator":
                        text_speech=pyttsx3.init()
                        text_speech.say("opening calculator")
                        text_speech.runAndWait()
                        subprocess.call("calc.exe")
                    elif a=="open paint" or  a=="paint" or a=="open microsoft paint" or a=="open ms paint":
                        text_speech=pyttsx3.init()
                        text_speech.say("opening paint")
                        text_speech.runAndWait()
                        subprocess.call("mspaint.exe")
                    elif a=="do google search" or a=="search" or a=="google search" or a=="do search" or a=="please search":
                        print(Fore.GREEN,"please press 1 for writting and 2 for speaking: ")
                        r=int(input())
                        if r==1:
                            s=input("Please provide about what you are trying to seach: ")
                        elif r==2:
                            t=sr.Recognizer()
                            with sr.Microphone() as source:
                                print(Fore.GREEN,"say something...")
                                audio=t.listen(source)
                            try:
        
                                s=t.recognize_google(audio)
                            except:
                                print(Fore.RED,"sorry could not recognize")
                        else:
                             print(Fore.RED,"should be 1 or 2")      
                        arr=s.split()
        
                        output="+".join(arr)
        
                        total="https://www.google.com/search?q="+output
                        webbrowser.open(total)
                    elif a=="evil" or a=="demon" or a=="bad power" or a=="evil power":
                        h=random.randint(1,2)
                        if h==1:
                            webbrowser.open("https://rajib3728.github.io/i-am-ghost/")
                        else:
                            webbrowser.open("https://rajib3728.github.io/virus/")
                    elif a=="take screenshot" or a=="please take screen shot":
                        myScreenshot = pyautogui.screenshot()
                        myScreenshot.save('E:\your_screenshot.png')
                        messagebox.showinfo("info","screen shot ✔ check e drive") 
                    elif a=="open camera" or a=="camera" or a=="please open camera":
                        text_speech=pyttsx3.init()
                        text_speech.say("opening camera")
                        text_speech.runAndWait()
                        subprocess.run('start microsoft.windows.camera:', shell=True)
                except:
                    print(Fore.RED,"sorry could not recognize")
        else:
            messagebox.showinfo("info","Please check internet connection!")
ans=True
for i in range(9):
    
    if i==1:
        print("**         **") 
    elif i==4:
        print("*************      **")
        print("*************      **")
    else:
        print("**         **      **")
x=input("Please provide Your name : ")
messagebox.showinfo("Info","hello! "+x+" Welcome to this application")
while(ans):

    play.playing(x)
    i=input("Press c to continue else other button to exit: ")
    if i.lower()=="c":
        ans=True
    else:
        ans=False

