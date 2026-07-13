import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import datetime
from plyer import notification
import pyautogui
import wikipedia
import pywhatkit as pwk
import user_config
import smtplib, ssl
import openai_request as ai
import image_generation
import mtranslate

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def command():
    content = " "
    while content == " ":
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening")
            audio = r.listen(source)
        try:
           content = r.recognize_google(audio)
           print("Google Speech Recognition thinks you said " +content)
        except Exception as e:
            print("Please try again")

    return content

def main_process():
    while True:
        request = command().lower()
        if "hello" in request:
            speak("Welcome, How can I help you?")
        elif "Play music" in request:
            speak("Playing music")
            song = random.randint(1,5)
            if song == 1:
                webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
            elif song == 2:
                webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
            elif song == 3:
                webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        elif "new task" in request:
            task = request.replace("new task", "")
            task = task.strip()
            if task != "":
                speak("Adding task: " + task)
                with open ("todo.txt","a") as file:
                    file.write(task + "\n")
        elif "show work" in request:
            with open("todo.txt","r") as file:
                tasks = file.read()
            notification.notify(title="Today's Work",
                                message=tasks)
        elif "open" in request:
            query = request.replace("open", "")
            pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.sleep(2)
            pyautogui.press("enter")

        elif "wikipedia" in request:
            request = request.replace("jarvis ", "")
            request = request.replace("search wikipedia ", "")
            result = wikipedia.summary(request, sentences=2)
            speak(result)

        elif "search google" in request:
            request = request.replace("search google ", "")
            webbrowser.open("https://www.google.com/search?q=" + request)

        elif "image" in request:
            request = request.replace("image ", "")
            image_generation.generate_image(request)

        elif "ask ai" in request:
            jarvis_chat = []
            request = request.replace("jarvis ", "")
            request = request.replace("ask ai ", "")
            jarvis_chat.append({"role": "user", "content": request})

            response = ai.send_request(jarvis_chat)

            speak(response)
        elif "clear chat" in request:
            jarvis_chat = []
            speak("Chat Cleared")
        else:
            request = request.replace("jarvis ", "")

            jarvis_chat.append({"role": "user", "content": request})
            response = ai.send_request(jarvis_chat)

            jarvis_chat.append({"role": "assistant", "content": response})
            speak(response)



if __name__ == "__main__":
    main_process()