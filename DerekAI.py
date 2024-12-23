import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def talk(text): 
    engine.say(text)
    engine.runAndWait()


def talk_command():   
    try:
        with sr.Microphone() as source:
            print("Listening...") 
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'Derek' in command: 
                command = command.replace('Derek','')
                print (command)
            
    except Exception as e:
        print("Error: " + str(e))
    return command

def run_alexa():
    command = talk_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is '+time)
    elif 'who is' in command:
        person = command.replace('who is ','')
        info = wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again')

    

while True:
    run_alexa()
