import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import subprocess
import webbrowser

#เปิดตัวแปรสำหรับ speeach recognizer 
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) #set รูปแบบเสียง


def talk(text):     #ฟังชั่นพูดที่จะใช้ใน command
    engine.say(text)
    engine.runAndWait()


def take_command():     #ฟังชั่น เช็คว่าพูด pk ละจะทำงานต่อ
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)  # รับเสียงจากไมค์
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'pk' in command:
                command = command.replace('pk', '')     # ลบคำว่า pk ละนำ command ไปใช้ต่อในฟังชั่นถัดๆไป
                print(command)
    except:
        pass
    return command


def run_pk():
    command = take_command()
    print(command)

    #command เฉพาะ
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'wiki' in command:
        wiki = command.replace('wiki', '')
        info = wikipedia.summary(wiki, 1)
        print(info)
        talk(info)
    elif 'search' in command:
        search = command.replace('search', '')
        talk('searching ' + search)
        pywhatkit.search(search)

    #command เปิดแอปตามตำแหน่งไฟล์
    elif 'line' in command:
        talk('openning line')
        subprocess.call('C://Users//User//AppData//Local//LINE//bin//LineLauncher.exe')
    elif 'court' in command:
        talk('openning Virsual Code')
        subprocess.call('C://Users//User//AppData//Local//Programs/Microsoft VS Code//Code.exe')

    #command เปิดเว็บตาม url
    elif 'youtube' in command:
        talk('openning Youtube')
        webbrowser.get('chorme',webbrowser.open_new_tab('https://www.youtube.com'))
    elif 'purple' in command:
        talk('openning twitch')
        webbrowser.get('chorme',webbrowser.open_new_tab('https://www.twitch.tv'))
    elif 'facebook' in command:
        talk('openning facebook')
        webbrowser.get('chorme',webbrowser.open_new_tab('https://www.facebook.com'))
    elif 'facebook' in command:
        talk('openning facebook')
        webbrowser.get('chorme',webbrowser.open_new_tab('https://www.facebook.com'))

    #command คำถามต่างๆเฉพาะ
    elif 'explain' in command:
        talk('i am a personal assistant that can do some of the basic application fuction')
    elif 'what can you do' in command:
        talk('i can do various thin like open youtube search google or open some application on pc')
    
while True:
    run_pk()
