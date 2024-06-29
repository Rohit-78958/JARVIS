import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
import google.generativeai as genai
import os
import musicLibrary

r = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150) 

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(command):
    if "open google" in command.lower():
        webbrowser.open("https://google.com")    
    elif "open youtube" in command.lower():
        webbrowser.open("https://youtube.com")    
    elif "open gmail" in command.lower():
        webbrowser.open("https://gmail.com")  
    elif "news" in command.lower():
        # Replace the # with the actual API key
        url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=#"
        # Make a GET request and parse the JSON response
        response = requests.get(url)
        data = response.json()

        # Extract titles (assuming the key is 'title')
        titles = [item.get("title", None) for item in data["articles"]]

        # Print the titles
        # Assuming 'titles' is a list containing article titles
        for i, title in enumerate(titles):
            if i >= 8:
                break
            speak(title)

    elif command.lower().startswith("play"):
        print(command.lower())
        typeOfSong = command.split(" ")[1]
        webbrowser.open(musicLibrary.music[typeOfSong])

    else:
        # Configure your API key
        genai.configure(api_key="#-4")

        # Create a model (e.g., 'gemini-1.0-pro-latest')
        # model = genai.GenerativeModel('gemini-1.0-pro-latest')
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(command+"Please keep response small!")
        speak(response.text)
        # print(response.text)

        


if __name__ == "__main__":
    speak("Initializing Jarvis....")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                r.adjust_for_ambient_noise(source, 1) 
                audio = r.listen(source, timeout=3, phrase_time_limit=2)

            start = r.recognize_google(audio)
            print(start)
            if "jarvis" in start.lower():
                speak("Yes Rohit!")

                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source, timeout=3, phrase_time_limit=2)

                    command = r.recognize_google(audio)
                    r.adjust_for_ambient_noise(source, 1) 
                    processCommand(command)

        except Exception as e:
            print("{0}".format(e))
