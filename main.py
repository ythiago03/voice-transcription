import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()

while True:

  try:
      print("Ouvindo...")
      with sr.Microphone() as mic:
         
         recognizer.adjust_for_ambient_noise(mic, duration=0.2)
         audio = recognizer.listen(mic)
         text = recognizer.recognize_google(audio, language="pt-BR")
         text.lower()
        
         print(f"Escutou:  {text}")
  
  except sr.UnknownValueError:
     
      recognizer = sr.Recognizer()
      continue