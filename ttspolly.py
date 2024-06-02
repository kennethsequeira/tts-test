import time
import speech_recognition as sr
from googletrans import Translator
from textblob import TextBlob
import boto3
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# AWS config
AWS_ACCESS_KEY = os.environ.get("AWS_ACCESS_KEY")
AWS_SECRET = os.environ.get("AWS_SECRET")



# Initialize speech recognition
r = sr.Recognizer()

# Initialize translator
translator = Translator()

# Initialize Polly client
polly_client = boto3.client('polly',
                            aws_access_key_id=AWS_ACCESS_KEY,
                            aws_secret_access_key=AWS_SECRET,
                            region_name='us-east-1')

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
    response = polly_client.synthesize_speech(Text=text, OutputFormat='mp3', VoiceId='Aditi')
    with open('output.mp3', 'wb') as f:
        f.write(response['AudioStream'].read())
    # Play the audio file (assuming you have a player installed)
    import os
    os.system("mpg321 output.mp3")

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
