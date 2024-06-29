import speech_recognition as sr
import webbrowser
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)  

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("munni badnaam hui darling tere liye")

    
