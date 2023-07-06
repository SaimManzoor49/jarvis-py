# from flask import Flask, request, jsonify
# import pyttsx3
# import speech_recognition as sr
# import datetime
# import wikipedia
# import webbrowser
# import os
# from flask_cors import CORS

# import smtplib

# app = Flask(__name__)
# # CORS(app)
# CORS(app, resources={r"/api/*": {"origins": "*"}})

# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)


# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()


# def wishMe():
#     hour = int(datetime.datetime.now().hour)
#     if 0 <= hour < 12:
#         speak("Good Morning!")
#     elif 12 <= hour < 18:
#         speak("Good Afternoon!")
#     else:
#         speak("Good Evening!")
#     speak("I am Jarvis. Please tell me how may I help you")


# def process_command(command):
#     if 'wikipedia' in command:
#         speak('Searching Wikipedia...')
#         query = command.replace("wikipedia", "")
#         results = wikipedia.summary(query, sentences=2)
#         speak("According to Wikipedia")
#         return results

#     elif 'open youtube' in command:
#         webbrowser.open("https://www.youtube.com/")
#         return "Opening YouTube..."

#     elif 'open google' in command:
#         webbrowser.open("https://www.google.com/")
#         return "Opening Google..."

#     elif 'open stackoverflow' in command:
#         webbrowser.open("https://www.stackoverflow.com/")
#         return "Opening Stack Overflow..."

#     elif 'play music' in command:
#         music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
#         songs = os.listdir(music_dir)
#         os.startfile(os.path.join(music_dir, songs[0]))
#         return "Playing music..."

#     elif 'the time' in command:
#         str_time = datetime.datetime.now().strftime("%H:%M:%S")
#         return f"Sir, the time is {str_time}"

#     elif 'open code' in command:
#         code_path = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
#         os.startfile(code_path)
#         return "Opening Visual Studio Code..."

#     elif 'email to harry' in command:
#         try:
#             speak("What should I say?")
#             content = takeCommand()
#             to = "harryyourEmail@gmail.com"
#             sendEmail(to, content)
#             return "Email has been sent!"
#         except Exception as e:
#             print(e)
#             return "Sorry, I am not able to send this email"


# def takeCommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold = 1
#         audio = r.listen(source)

#     try:
#         print("Recognizing...")
#         query = r.recognize_google(audio, language='en-in')
#         print(f"User said: {query}\n")
#         return query
#     except Exception as e:
#         print("Say that again please...")
#         return "None"


# @app.route('/api/voice-command', methods=['POST'])
# def handle_voice_command():
#     data = request.get_json()
#     message = data['message']
#     # 
#     print(data)

#     result = process_command(message)

#     response = jsonify({'result': result})
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     response.headers.add('Access-Control-Allow-Headers', 'Content-Type')

#  return response
#     # return jsonify({'result': result})


# if __name__ == "__main__":
#     wishMe()
#     app.run()



from flask import Flask, request, jsonify
from flask_cors import CORS
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis. Please tell me how may I help you")


def process_command(command):
    if 'wikipedia' in command:
        speak('Searching Wikipedia...')
        query = command.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        return results

    elif 'open youtube' in command:
        webbrowser.open("https://www.youtube.com/")
        return "Opening YouTube..."

    elif 'open google' in command:
        webbrowser.open("https://www.google.com/")
        return "Opening Google..."

    elif 'open stackoverflow' in command:
        webbrowser.open("https://www.stackoverflow.com/")
        return "Opening Stack Overflow..."

    elif 'play music' in command:
        music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[0]))
        return "Playing music..."

    elif 'the time' in command:
        str_time = datetime.datetime.now().strftime("%H:%M:%S")
        return f"Sir, the time is {str_time}"

    elif 'open code' in command:
        code_path = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(code_path)
        return "Opening Visual Studio Code..."

    elif 'email to harry' in command:
        try:
            speak("What should I say?")
            content = takeCommand()
            to = "harryyourEmail@gmail.com"
            sendEmail(to, content)
            return "Email has been sent!"
        except Exception as e:
            print(e)
            return "Sorry, I am not able to send this email"


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query
    except Exception as e:
        print("Say that again please...")
        return "None"


@app.route('/api/voice-command', methods=['POST'])
def handle_voice_command():
    data = request.get_json()
    message = data['message']
    print(message)
    result = process_command(message)
    print(result)

    return jsonify({'result': result})


if __name__ == "__main__":
    wishMe()
    app.run()
