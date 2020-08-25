import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
# import pyautogui  
import psutil
import pyjokes


engine=pyttsx3.init("sapi5")
# engine.say('Hello tushar bansal')
# engine.runAndWait() 

def speak(audio):
    engine.say(audio)
    engine.runAndWait() 

def time():
    speak('The current time is ')
    # Time = datetime.datetime.now().strftime('%I:%M:%S')
    Time = datetime.datetime.now().strftime('%H:%M:%S')
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak('The current date is')
    speak(date)
    speak(month)
    speak(year)


def wishme():
    speak('Welcome back sir!')

    hour=datetime.datetime.now().hour

    if hour>=6 and hour<12:
        speak('Goog morning')
    elif hour>=12 and hour<=16:
        speak('Good afternoon')
    elif hour>16 and hour<=21:
        speak('good evening')
    else:
        speak('good night')
        
    speak('Siri at your service! How can i help you ?')


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-US')
        print(query)
    except Exception as e:
        print(e)
        speak('Say that again please...')

        return 'None'
    
    return query

def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('bansaltushar1213@gmail.com','Tushar@1213')
    server.sendmail('bansaltushar1213@gail.com', to, content)
    server.close()

# def screenshot():
#     img = pyautogui.screenshot()
    # img.save('E:\udemy\ss.png')


def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at ' + usage)

    battery = psutil.sensors_battery().percent
    speak('battery is at')
    speak(battery)


def jokes():
    speak(pyjokes.get_joke())


if __name__=='__main__':
    
    wishme()
    
    while True:
        query = takeCommand().lower()
        
        if 'time' in query:
            time()

        elif 'date' in query:
            date()

        elif 'offline' in query:
            speak('Thank you so much sir')
            quit()

        elif 'wikipedia' in query:
            speak(f'getting results for...{query}')
            query = query.replace('wikipedia','')
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
            chromepath = "D:/programs/Mozilla Firefox/firefox.exe %s"
            search = takeCommand().lower()
            search = search.replace(" ", "_")
            wb.get(chromepath).open_new_tab("https://en.wikipedia.org/wiki/"+ search + ".com")

        elif "email" in query:
            try:
                speak('what should i say?')
                content = takeCommand()
                to = 'tusharbansal1308@gmail.com'
                sendmail(to,content)
                speak(content)

            except Exception as e:
                print(e)
                speak('Unable to send the message')

        elif 'search' in query:
            speak('what should i search?')
            chromepath = "D:/programs/Mozilla Firefox/firefox.exe %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")

        elif 'log out' in query:
            os.system('shutdown - 1')

        elif 'shutdown' in query:
            os.system('shutdown /s /t 1')
 
        elif 'restart' in query:
            os.system('shutdown /r /t 1')

        # elif 'play songs' in query:
        #     songs_dir = 'F:\musics\music'
        #     songs = os.listdir(songs_dir)
        #     os.startfile(os.path.join(songs_dir, songs[0])
    
        elif "remember that" in query:
            speak('what should i remember?')
            data = takeCommand()
            speak('you said me to remember' + data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()
        
        elif 'do you know anything' in query:
            remember = open('data.txt','r')
            speak('you said me to remeber that ' + remember.read())

        # elif 'screenshot' in query: 
        #     screenshot()
        #     speak('Done')

        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            jokes()