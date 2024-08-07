import pyttsx3  # It's Text to speech package
import webbrowser  # webbrowser = used to open and Operate browser
import speech_recognition as sr
import music_library
import requests
from openai import OpenAI  # paid
from gtts import gTTS  # paid
import pygame
import os

# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:

# obtain audio from the microphone
recognizer = sr.Recognizer()
# recognizer  = this object is used to recognize word spoken by user

engine = pyttsx3.init()
# initialize pyttsx

newsapi = ""
# it's api for news from "https://newsapi.org/"


def speke(text):
    # engine.say("")
    engine.say(text)
    engine.runAndWait()


def new_speke(text):
    tts = gTTS(text)

    audio_file = "temp.mp3"
    tts.save(audio_file)
    # Initialize Pygame
    pygame.init()

    # Initialize the mixer module for audio
    pygame.mixer.init()
    
    # Load and play the MP3 file
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()

    # Keep the program running until the audio finishes playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove(audio_file)

    # Quit Pygame
    pygame.quit()


def aiProcess(command):
    client = OpenAI(
        api_key="",
    )

    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alaxa and Google Cloude. Give pointwise, short and simple response.please",
                },
                {
                    "role": "user",
                    "content": command,
                },
            ],
        )

        return completion.choices[0].message.content

    except client.error.OpenAIError as e:
        print(f"An error occurred: {e}")
        return None


def processCommand(x):

    data = x.lower()
    print(data)

    if "open google" in data:
        webbrowser.open("https://www.google.com/")

    elif "open github" in data:
        webbrowser.open("https://github.com/sandip3")

    elif "open manga hub" in data:
        webbrowser.open("https://managahub.io")

    elif "open youtube" in data:
        webbrowser.open("https://www.youtube.com/")

    elif "open chat gpt" in data:
        webbrowser.open("https://chatgpt.com/")

    elif "open linkedin" in data:
        webbrowser.open("https://www.linkedin.com/in/sandip-mishra-74906b258/")

    elif data.startswith("play"):
        song = data[len("play ") :]
        link = music_library.music[song]
        webbrowser.open(link)

    elif "news" in data:
        r = requests.get(
            f"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey={newsapi}"
        )
        # Check if the request was successful
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()

            # Extract articles
            articles = data.get("articles", [])

            # Extract and print titles
            for i, article in enumerate(articles):
                title = article.get("title", "No title available")
                speke(f"Article {i + 1}: {title}")
        else:
            speke("Failed to retrieve data:", r.status_code)

    else:
        # let OpenAI handle Reqest
        output = aiProcess(data)
        speke(output)


if __name__ == "__main__":
    speke("Initialize Jarvis......")

    while True:
        # wait for "Wake-word" = "Jarvis"

        # recognize speech using Google recognizer
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)

                # Listening...
                print("\nListening...")

                # Audio capturing
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=2)

            # Recognizing...
            print("Recognizing...")

            Word = recognizer.recognize_google(audio)
            if Word.lower() == "jarvis":
                speke("Yes, master")

                # Listen for Command
                with sr.Microphone() as source:

                    recognizer.adjust_for_ambient_noise(source)
                    print("\nJarvis Activating...")
                    print("\nListening...")

                    # Audio capturing
                    audio = recognizer.listen(source)

                    print("Recognizing...")
                    command = recognizer.recognize_google(audio)

                    processCommand(command)

        except Exception as x:
            print(f"Error : {x}")
