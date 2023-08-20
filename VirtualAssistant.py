import smtplib
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import requests
import json
import overpy
from translate import Translator
from bs4 import BeautifulSoup


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
        engine.say(audio)
        engine.runAndWait()


def time():
        Time = datetime.datetime.now().strftime("%I:%M:%S")
        speak(f'The current time is {Time}')

def wiki():
        question = input("What do you wanna know?")
        result = wikipedia.summary(question, sentences=1)
        speak("According to wikipedia")
        print(result)
        speak(result)

def takeCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing..")
            query = r.recognize_google(audio, language='en-in')
            print(f"You said : {query}\n")


        except Exception as e:
            print(e)
            print("Please Say that again...")
            speak("Please Say that again...")
            takeCommand()

        return query

def hearJoke():
        try:
            r = requests.get("https://v2.jokeapi.dev/joke/Any?blacklistFlags=religious&format=txt")
            r.raise_for_status()
            joke = r.text
            print(joke)
            speak(joke)

        except Exception as e:
            print(e)
            print("\033[91mAn error occurred while fetching a joke\033[0m")
            speak("An error occurred while fetching a joke")

def getFacts():
        try:
            r = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
            r.raise_for_status()
            data = r.json()
            fact = data["text"]
            print(fact)
            speak(fact)
        except Exception as e:
            print(e)
            print("\033[91mAn error occurred while fetching a fun fact.\033[0m")
            speak("An error occurred while fetching a fun fact")

def getWeather():
        location = input("Enter your location:\n")
        location = "Weather in " + location
        url = f"https://www.google.com/search?&q={location}"

        try:
            r = requests.get(url)
            r.raise_for_status()
            s = BeautifulSoup(r.text, "html.parser")

            update = s.find("div", class_="BNeawe iBp4i AP7Wnd").get_text() if s.find("div",
                                                                                      class_="BNeawe iBp4i AP7Wnd") else "Weather information not found"
            print(update)

        except Exception as e:
            print("\033[91mAn error occurred while fetching weather update\033[0m")
            speak("An error occurred while fetching weather update")

def sendEmail():
        speak("Enter the valid email of the recipient")
        to = input("Enter the email of the recipient")
        speak("Enter the content of your email")
        email = input("Enter the content of your email")

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login('khizarahmed3@gmail.com', 'wzjlmuswfnxlgivr')
            server.sendmail('khizarahmed3@gmail.com', to, email)
            server.close()
            print("Email sent successfully")
            speak("Email sent successfully")

        except Exception as e:
            print(e)
            speak("An error occurred while sending the email")

def getNearbyPlaces():
        api = overpy.Overpass()

        speak("Enter the latitude of the location")
        latitude = float(input("Enter latitude of the location:\n"))

        speak("Enter the longitude of the location")
        longitude = float(input("Enter the longitude of the location:\n"))

        speak("Enter the amenity type")
        amenity_type = input("Enter the amenity type:\n")

        distance = 1000  # 1 kilometer

        result = api.query(f"""
            [out:json];
            node(around:{distance}, {latitude}, {longitude})["amenity"="{amenity_type}"];
            out;
        """)

        x = 0
        if result.nodes:
            for node in result.nodes:
                print(node.tags["name"], ":", node.tags["amenity"])
                name = node.tags["name"]
                speak(name)
                x += 1
                if x == 3:
                    break
        else:
            print("No results found")
            speak("No results found")
def takeQuiz():
        flag = True
        print("*****WELCOME TO QUIZ GAME*****\n")
        speak("WELCOME TO QUIZ GAME")
        while flag:
            r = requests.get("https://opentdb.com/api.php?amount=1&category=15&difficulty=easy&type=multiple")
            question = json.loads(r.text)
            print(question['results'][0]['question'])
            q = question['results'][0]['question']
            speak(q)
            print("", question['results'][0]['correct_answer'], "\n", question['results'][0]['incorrect_answers'][0],
                  "\n",
                  question['results'][0]['incorrect_answers'][1], "\n", question['results'][0]['incorrect_answers'][2])

            ans = input("\nPlease select your answer")
            if (ans == question['results'][0]['correct_answer']):
                print("Correct Answer!")
                speak("Correct Answer!")
            else:
                print("Incorrect answer")
                speak("Incorrect answer")
            user = input("Enter 'Q' to quit or 'R' to play again")
            if (user.lower() == 'q'):
                flag = False
            else:
                continue

def search_books_by_genre():
        BASE_URL = "https://openlibrary.org"
        SEARCH_URL = "/search.json"
        speak("Enter a genre")
        genre = input("Enter a genre: ")

        params = {"q": f"subject:{genre}"}
        response = requests.get(BASE_URL + SEARCH_URL, params=params)
        search_results = response.json()
        suggested_books = []
        if "docs" in search_results:
            for i, book in enumerate(search_results["docs"][:2]):
                title = book.get("title", "Title not available")
                author = book.get("author_name", ["Author not available"])[0]
                suggested_books.append((title, author))

        print(f"Suggested Books in the {genre} genre:\n")
        speak(f"Suggested Books in the {genre} genre:")
        for i, (title, author) in enumerate(suggested_books, start=1):
            print(f"{i}. Title: {title} | Author: {author}")
            speak(f"{i}. Title: {title} | Author: {author}")

def translateText():
    speak("Enter the text you want to translate")
    text = input("Enter the text that you want to translate :\n")
    speak("Enter the language you want it to translate to")
    target_lang = input("Enter the language that you want the text translated to (Enter es for spanish fr fron french etc):\n")

    translator = Translator(to_lang = target_lang)
    translated_text = translator.translate(text)
    print("Translated text :\n"+translated_text)
    speak(translated_text)


