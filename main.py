import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import wolframalpha
import time
import smtplib
import psutil
import pyautogui
import webbrowser
from tkinter import *
from tkinter.ttk import *
from time import strftime
import cv2

listener = sr.Recognizer()
engine = pyttsx3.init()
wolframalpha_app_id = 'abc123@gmail.com'
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#cap = cv2.VideoCapture(0)
#def face_detection():
#     while True:
#         a, img = cap.read()
#        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#         faces = face_cascade.detectMultiScale(gray, 1.1, 4)
#         for (x,y,w,h) in faces:
#             cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0 , 0), 2)
#         cv2.imshow('img', img)
#         k = cv2.waitKey(30) & 0xff
#         if k==27:
#             break

def talk(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    talk('welcome back Boss!')
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        talk('Good Morning Boss!')
    elif hour>= 12 and hour<18:
        talk('Good Afternoon Boss!')
    else:
        talk('Good Evening Boss!')
    assname = ('jarvis')
    talk('i am your assistant')
    talk(assname)
root = Tk()
root.title("clock")
def clock():
    string = strftime('%H:%M:%S: %p')
    label.config(text=string)
    label.after(1000, clock)
label = Label(root, font=("ds-digital", 80), background ="black", foreground ="cyan")
label.pack(anchor='center')

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognizing...')
        command = listener.recognize_google(audio)
        print(f"User said: {command}\n")
    except Exception as e:
        print(e)
        print('Unable to Recognize your voice.')
        return 'None'
    return command

def time():
    time.localtime()
    time.strftime('%M:%S')


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('abc123@gmail.com', '123456')
    server.sendmail('abc123@gmail.com', to, content)
    server.close()

#def screenshot():
#    img = pyautogui.screenshot()
#    img.save('C:\Users\Admin\Pictures\Camera Roll')

def cpu():
    usage = str(psutil.cpu_percent())
    print('CPU is at' +usage)
    talk('CPU is at' +usage)
    battery = psutil.sensors_battery()
    print('battery is at')
    print(battery)
    talk('battery is at')
    talk(battery)

if __name__ == '__main__':
    clear = lambda : os.system('cls')
    clear()
    face_detection()
    cap.release()
    clock()
    mainloop()
    wishMe()

    while True:

        command = take_command().lower()
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing' + song)
            pywhatkit.playonyt(song)

        elif 'open stackoverflow' in command:
            talk('Here you go to Stack Over flow. Happy Coding')
            webbrowser.open('stackoverflow.com')
        elif 'send email' in command:
            try:
                talk('what should I say?')
                content = take_command()
                talk('whom should i send')
                to = take_command()
                sendEmail(to, content)
                talk('Email has been send.')
            except Exception as e:
                print(e)
                talk('I am not able to send this email')
        if 'message priya' in command:
            message = command.replace('message priya', '')
            talk('sending' + message)
            # a = datetime.datetime.now().strftime('%M')
            # b = datetime.datetime.now().strftime('%S')
            pywhatkit.sendwhatmsg('+919080498840', message, time())
        if 'message siri' in command:
            message = command.replace('message siri', '')
            talk('sending ' + message)
            pywhatkit.sendwhatmsg('+917695875138', message, time())
        if 'search google' in command:
            search = command.replace('search google', '')
            talk('searching' + search)
            pywhatkit.search(search)
        elif 'cpu usage' in command or 'show battery level' in command:
            cpu()
        elif 'go offline' in command:
            talk('Going Offline sir!')
            quit()
        elif 'open pictures' or 'show pictures' in command:
            talk('opening picture location...!')
            picture = r'C:\Users\Admin\Pictures'
            os.startfile(picture)
        elif 'open documents' or 'show documents' in command:
            talk('opening document location...!')
            document = r'C:\Users\Admin\Documents'
            os.startfile(document)
        elif 'open music' or 'show music' in command:
            talk('opening music location...!')
            music = r'C:\Users\Admin\Music'
            os.startfile(music)
        elif 'open videos' in command:
            talk('opening videos location...!')
            videos = r'C:\Users\Admin\Videos'
            os.startfile(videos)
        elif 'open downloads' or 'show downloads' in command:
            talk('opening downloads location...!')
            downloads = r'C:\Users\Admin\Downloads'
            os.startfile(downloads)
        elif 'open marvel file' or 'show marvel files' in command:
            talk('Opening mahabharat file location...!')
            mahabharat = r'E:\Marvel'
            os.startfile(mahabharat)
        elif 'open this pc' in command:
            talk('opening this pc...')
            this_pc = r'C:\Users\Admin\Desktop\This PC - Shortcut.lnk'
            os.startfile(this_pc)
        elif 'note' or 'note this' in command:
            talk('What should I write, Sir?')
            notes = take_command()
            file = open('notes.txt', 'w')
            talk('Sir, Should i include date and time')
            snfm = take_command()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime('%I:%M:%s')
                file.write(strTime)
                file.write(' :- ')
                file.write(notes)
            else:
                file.write(notes)
            talk('Done Taking Notes, Sir!')
        elif 'show notes' in command:
            talk('showing notes')
            file = open('note.txt', 'r')
            print(file.read())
            talk(file.read())
        elif 'jarvis' in command:
            wishMe()
            talk('Jarvis 1 point 0 in your service Sir')
            talk('what can i do for you sir')
        elif 'weather' in command:
            city = take_command()
            pywhatkit.search('weather')
        elif 'screenshot' in command:
            screenshot()
        elif 'will you be my girlfriend' in command or 'will you be my boyfriend' in command:
            talk("I'm not sure about, may be you should give me some time")
        elif 'today date' in command or 'what the date today' in command:
                year = datetime.datetime.now().year
                month = datetime.datetime.now().month
                date = datetime.datetime.now().day
                talk('the current date is')
                talk(date)
                talk(month)
                talk(year)
        elif 'shut down' in command:
            print('Shut downing...')
            os.system("shutdown /s /t 1")
        elif 'time' in command:
            date = datetime.datetime.now().strftime('%I:%M %p')
            print(date)
            talk(f"Sir, the time is " + date)
        elif 'who is' in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 3)
            print(info)
            talk(info)
        elif 'stop listening' in command:
            talk('for how much time you want to stop jarvis from listening commands')
            a = int(take_command())
            time.sleep(a)
            print(a)
        elif 'date with me' in command:
            talk('haha Sorry . i have headache')
        elif 'thank you' in command:
            talk("It's my pleasure Boss!")
        elif 'you are so sweet' in command:
            talk('You also sweet person Boss!')
        elif 'sorry' in command:
            talk("Don't tell sorry sir!. It's my fault")
            talk('Sorry Boss!')
        elif 'it is ok' in command:
            talk("you are white hearted person Boss")
        elif 'are you single' in command:
            talk('I am in a relationship with wifi')
        elif 'what is your job' in command or 'what is your work' in command:
            talk('i am your assistant . My work is Searching what you want to telling')
        elif 'do you speak tamil' in command:
            talk('No sir!. but i know tamil and all languages')
        elif 'do you speak english' in command:
            talk('Yes sir!. I am speak english well')
        elif 'who are you' in command:
            talk('i am your personal assistant . my name is jarvis . made in python codes')
        elif 'joke' in command:
            print(pyjokes.get_joke())
            talk(pyjokes.get_joke())
        elif 'remember that' in command:
            talk('what should i remember?')
            memory = take_command()
            talk('you asked me to remember that' + memory)
            remember = open('memory.txt', 'w')
            remember.write(memory)
            remember.close()
        elif 'do you remember anything' in command:
            remember = open('memory.txt', 'r')
            talk('you asked me to remember that' + remember.read())
        elif 'where is' in command:
            command = command.replace('where is', '')
            location = command
            talk('User asked to locate' + location)
            webbrowser.open('https://www.google.com/maps/place/' + location + '')
        elif 'calculate' in command:
            client = wolframalpha.Client(wolframalpha_app_id)
            index = command.lower().split().index('calculate')
            command = command.split()[index + 1:]
            res = client.command(''. join(command))
            answer = next(res.results).text
            print('The Answer is : '+answer)
            talk('The Answer is : '+answer)
        elif 'about love' in command:
            print('love is chemical reaction humans body and also 7th sense of humans')
            talk('love is chemical reaction humans body and also 7th sense of humans')
        elif 'i love you' in command:
            print('it is hard to understand')
            talk('it is hard to understand')
        elif 'how are you' in command:
            print('I am fine . How are you Boss?')
            talk('I am fine . How are you Boss?')
        elif 'fine' in command or 'good' in command:
            print("It's good to know that your fine")
            talk("It's good to know that your fine")
        elif 'not fine' in command:
            print("It's bad news for me . Get will soon Boss")
            talk("It's bad news for me . Get will soon Boss")
        elif "I'm feel lonely" in command or "I'm feel alone" in command:
            print("Don't Worry Boss!. I'm Always with you")
            talk("Don't Worry Boss!. I'm Always with you")
        elif 'change my name to' in command:
            command = command.replace('change my name to', '')
            assname = command
        elif 'change name' in command:
            talk('What would you like to call me, Boss')
            assname = take_command()
            talk('Thanks for naming me')
        elif "what's your name" in command or 'what is your name' in command:
            talk('My friends call me')
            talk('Jarvis')
            print('my friends call me jarvis')
        elif 'who made you' in command or 'who created you' in command:
            talk('I have been created by Gowthaman Arul')
        elif 'who am i' in command:
            talk('If you talk then definitely your human')
        elif 'sleep system' in command:
            print('system go to sleeping...!')
            talk('system go to sleeping...!')
            os.system('shutdown /h')
        elif 'log out system' in command:
            print('log outing System...!')
            talk('log outing System...!')
            os.system('shutdown -l')
        elif 'restart system' in command:
            print('restarting System....!')
            talk('restarting System....!')
            os.system('shutdown /r /t 1')

