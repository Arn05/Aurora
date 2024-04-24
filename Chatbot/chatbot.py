from flask import Flask, render_template, request
import speech_recognition as sr
import pyttsx3
import google.generativeai as genai

model = genai.GenerativeModel('gemini-pro')
app = Flask(__name__)

engine = pyttsx3.init()

def speak(text):
  engine.say(text)
  engine.runAndWait()

def listen():
  try:
    with sr.Microphone() as source:
      print("Listening...")
      audio = recognizer.listen(source)
      text = recognizer.recognize_google(audio)
      print("You said: " + text)
      return text
  except sr.UnknownValueError:
    print("Sorry, I could not understand audio")
  except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
  return None

recognizer = sr.Recognizer()

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
  user_input = request.form["user_input"]
  # Process user input (optional)
  # You can perform NLP tasks like intent recognition here
  prompt = user_input  # Replace with formulated prompt if needed
  response = model.generate_content("What is the meaning of life?")
  speak(response)
  return render_template("chat.html", user_input=user_input, response=response)

if __name__ == "__main__":
  app.run(debug=True)
