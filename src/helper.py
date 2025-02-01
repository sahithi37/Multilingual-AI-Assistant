import speech_recognition as sr
import google.generativeai as genai
from dotenv import load_dotenv
import os
from gtts import gTTS

# Load environment variables
load_dotenv()

# Geminiai API Key
GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"]=GOOGLE_API_KEY

if GOOGLE_API_KEY is None:
    raise ValueError("ERROR: OPENAI_API_KEY is not set. Check your .env file.")


# Function to capture voice input
def voice_input():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("✅ Recognized Speech:", text)
        return text
    except sr.UnknownValueError:
        print("❌ Could not understand audio")
        return "Error: Could not understand audio"
    except sr.RequestError as e:
        print(f"❌ API Request Error: {e}")
        return "Error: Could not process speech"

# Function to generate response using OpenAI GPT-4

def llm_model(user_text):
    #model = "models/gemini-pro"
    
    genai.configure(api_key=GOOGLE_API_KEY)
    
    model = genai.GenerativeModel('gemini-pro')
    
    response=model.generate_content(user_text)
    
    result=response.text
    
    return result

# Function to convert text to speech
def text_to_speech(text):
    tts = gTTS(text=text, lang="en")
    tts.save("speech.mp3")  # Save audio as MP3
