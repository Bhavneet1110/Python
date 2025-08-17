import pyttsx3                                  #importing main modules for program
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')                  #getting program ready to speak (text to speech)
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe() :                                  #making python wish me whenever I run the program according to the local time
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
       speak("Good Morning!, I am Jarvis sir. Tell me how can I help you!")


    elif hour >= 12 and hour<18:
       speak("Good Afternoon!, I am Jarvis sir. Tell me how can I help you!")


    else :
       speak("Good Evening!, I am Jarvis sir. Tell me how can I help you!") 
       


def takeCommand():                              #to take my voice as command
          
   r = sr.Recognizer()
   with sr.Microphone() as source:
      print("Listening...")
      r.pause_threshold = 1
      audio = r.listen(source)

   try:
      print("Recognizing...")
      query = r.recognize_google(audio, language='en-in')
      print(f"User said: {query}\n")
     
   except Exception as e:
      # print(e)
      print("Say that again please...")
      return "None"
   return query

if __name__ == "__main__": 
    wishMe()
    while True:
      query = takeCommand().lower()

      
      # Logic for executing tasks based on query
      
      if 'wikipedia' in query:                           #making it do main functions like opening google, asking
         speak('Searching Wikipedia...')
         query = query.replace("wikipedia", "")
         results = wikipedia.summary(query, sentences=2) 
         speak("According to Wikipedia")
         print(results)
         speak(results)

      elif "open youtube" in query:
         webbrowser.open('youtube.com')

      elif "open google" in query:
         webbrowser.open('google.com')

      elif "open stackoverflow" in query:
         webbrowser.open('stackoverflow.com')

      elif "play music" in query:
         music_dir = 'ThisPc \\ C: \\ Users \\ lenovo \\ Music'
         songs = os.listdir(music_dir)
         print(songs)
         os.startfile(os.path.join(music_dir, songs[0]))

      elif "the time" in query :
         strTime = datetime.datetime.now().strftime("%H:%M:%S")
         print(strTime)
         speak(f"sir the time is {strTime}")

      elif "open code" in query :
         codePath = "C :\\Users\\lenovo\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
         os.startfile(codePath)

      elif "open github" in query:
         webbrowser.open('github.com')

      







         

         