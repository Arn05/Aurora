import subprocess
import pyttsx3
import json
import speech_recognition as sr
import datetime
import webbrowser
import os
import ctypes
import time
import requests
import mysql.connector as sqlcon
from urllib.request import urlopen
import google.generativeai as genai


genai.configure(api_key='AIzaSyASZqZgHvFivk5xoXVN-p1cGGjOZ-_JMmw')
model = genai.GenerativeModel('gemini-pro')



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    
    speak("I am aurora")


assname = 'aurora'
def register():
    
    speak('You chose Register')
    print('You chose register. ')
    cursor = con.cursor()
    speak('Enter your username')
    name = input('Enter the username :- ')
    speak('Enter the password')
    password = input('Enter your password :- ')
    speak('Please confirm your password')
    conf_password = input('Please confirm your Password :- ')
    sqlform = "Insert into login_info values (%s,%s,%s) "
    users = [(name, password, conf_password)]
    if password == conf_password:
        cursor = con.cursor()
        cursor.executemany(sqlform, users)
        con.commit()
        print('You have successfully registered. You can now login.')
        speak('You have successfully registered. You can now login.')
        login()

    else:
        speak('The confirmed password does not match the password entered. Please try again .')
        print('The confirmed password does not match the password entered. Please try again .')
        print('--------' * 15)
        quit()




def login():
    speak('You chose Login')
    print('You chose Login.')
    cursor = con.cursor()
    speak('Enter your Username ')
    name = input('Enter the username :- ')
    speak('Enter the password ')
    Passwd = int(input('Enter the password :- '))
    sqlform="SELECT Password from login_info where name=(%s)"
    x=[name]
    cursor.execute(sqlform,x)
    result = cursor.fetchall()
    if int(result[0][0])==Passwd:
        speak("Hello, Welcome back")
        
    else:
        speak('Invalid Username or Password please try again')
        quit()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        takeCommand()
        return 0

    return query


def limit_output_to_words(text, max_words):
    words = text.split()
    selected_words = words[:max_words]
    limited_output = ' '.join(selected_words)
    return limited_output


#MYSQL-Connection:-
con = sqlcon.connect(host='localhost', user='root', password='1234', database='pbl_project')
cursor = con.cursor()
cursor.execute('use pbl_project;')
cursor.execute('create table if not exists login_info(Name varchar(30), password varchar(15), conf_password varchar(15));')

#program starts
wishMe()
speak('Would you like to login or register?')
query = takeCommand()

if 'register' in query:
    register()

elif 'login' in query:
    l=login()

    while query!="bye":

        query = takeCommand().lower()


        # All the commands said by user will be
        # stored here in 'query' and will be
        # converted to lower case for easily
        # recognition of command
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")

        elif 'bye' in query:
            speak("Bye! See you soon.")
            quit()

        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")


        elif 'play music' in query or "play song" in query:
            speak("Here you go with music")
            subprocess.Popen('C:\\Users\\Ajay\\AppData\\Roaming\\Spotify\\Spotify.exe')
            speak('Opening Spotify ')

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"Sir, the time is {strTime}")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            assname = query

        elif "change name" in query:
            speak("What would you like to call me, Sir ")
            assname = takeCommand()
            speak("Thanks for naming me")

        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak(assname)
            print("My friends call me", assname)

        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Arnav Wani.")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif "calculate" in query:

            subprocess.Popen('C:\\Windows\\System32\\calc.exe')
            speak('opening calculator')

        elif 'search' in query or 'play' in query:

            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.open(query)

        elif "who am i " in query:
            speak("If you speak then definitely your human.")

        elif "why you came to world" in query:
            speak("Thanks to Arnav. further It's a secret")

        elif 'PowerPoint presentation' in query:
            speak("opening Power Point presentation")
            power = "C:\\Users\\Ajay\\Desktop\\Minor Project\\Presentation\\Voice Assistant.pptx"
            os.startfile(power)

        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")

        elif "who are you" in query:
            speak("I am your virtual assistant created by Arnav")

        elif 'reason for you' in query:
            speak("I was created as a Minor project by Mister Arnav ")

        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,0,"Location of wallpaper",0)
            speak("Background changed successfully")

        elif 'news' in query:

            try:
                jsonObj = urlopen(
                    '''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''')
                data = json.load(jsonObj)
                i = 1

                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============''' + '\n')

                for item in data['articles']:
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:

                print(str(e))


        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin Recycled")

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop aurora from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")

        elif "camera" in query or "photo" in query:
            cam = Device()
            cam.saveSnapshot('C:\\Users\\Ajay\\PycharmProjects\\voice assistant\\auroracaputre.jpg')

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('aurora.txt', 'w')
            speak("Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime('%I:%M %p')
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show note" in query:
            speak("Showing Notes")
            file = open("aurora.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif "update assistant" in query:
            speak("After downloading file please replace this file with the downloaded one")
            url = '# url after uploading file'
            r = requests.get(url, stream=True)

            with open("Voice.py", "wb") as Pypdf:

                total_length = int(r.headers.get('content-length'))

                for ch in progress.bar(r.iter_content(chunk_size=2391975),
                                       expected_size=(total_length / 1024) + 1):
                    if ch:
                        Pypdf.write(ch)

        # NPPR9-FWDCX-D2C8J-H872K-2YT43
        elif "aurora" in query:

            wishMe()
            speak("aurora 1 point o in your service Mister")
            speak(assname)

        elif "weather" in query:

            # Google Open weather website
            # to get API of Open weather
            api_key = "Api key"
            base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
            speak(" City name ")
            print("City name : ")
            city_name = takeCommand()
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            response = requests.get(complete_url)
            x = response.json()

            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " + str(
                    current_temperature) + "\n atmospheric pressure (in hPa unit) =" + str(
                    current_pressure) + "\n humidity (in percentage) = " + str(
                    current_humidiy) + "\n description = " + str(weather_description))

            else:
                speak(" City Not Found ")

        
        elif "wikipedia" in query:
            webbrowser.open("wikipedia.com")

        elif "Good Morning" in query:
            speak("A warm" + query)
            speak("How are you Mister")
            speak(assname)

        # most asked question from google Assistant
        elif "will you be my gf" in query or "will you be my bf" in query:
            speak("I'm not sure about, may be you should give me some time")

        elif "how are you" in query:
            speak("I'm fine, glad you me that")

        elif "i love you" in query:
            speak("It's hard to understand")

        else:
            response = model.generate_content(query)
            
            count=0
            for i in response:
                if ' ' in response:
                    count+=1
            if count>=50:
                print(response.text)
            else:
                print(response.text)
                speak(response.text)
           

        '''else:
            response = gemini.text_generation(
            prompt=query,
            max_tokens=64,  # Adjust max_tokens as needed
            key='AIzaSyASZqZgHvFivk5xoXVN-p1cGGjOZ-_JMmw'  # Pass the API key here'''
else:
    speak("Could not login")

    # elif "" in query:
    # Command go here
    # For adding more commands
