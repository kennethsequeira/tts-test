import time
import speech_recognition as sr
from googletrans import Translator
from textblob import TextBlob
import pyttsx3

# Initialize speech recognition
r = sr.Recognizer()

# Initialize translator
translator = Translator()

# Initialize Text-to-Speech (TTS) engine
tts_engine = pyttsx3.init()

def transcribe_audio():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    
    try:
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results: {e}")
        return ""

def translate_text(text, target_language):
    translation = translator.translate(text, dest=target_language)
    return translation.text

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment
    return sentiment

def text_to_speech(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

def main():
    while True:
        # Step 1: Real-Time Transcription
        transcribed_text = transcribe_audio()
        
        # Step 2: Real-Time Translation
        translated_text = translate_text(transcribed_text, target_language='en')
        
        # Step 3: Sentiment Analysis
        sentiment = analyze_sentiment(translated_text)
        
        # Step 4: Text-to-Speech
        text_to_speech(translated_text)
        
        print("Translated Text:", translated_text)
        print("Sentiment:", sentiment)
        print("=" * 50)
        
        time.sleep(2)  # Adjust delay as needed

if __name__ == "__main__":
    main()
