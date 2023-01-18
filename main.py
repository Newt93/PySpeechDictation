import speech_recognition as sr

# Create a recognizer object
r = sr.Recognizer()

# Start listening to the microphone
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# Recognize the speech
try:
    text = r.recognize_google(audio)
    print(f"You said: {text}")
    # code here to type the text on a textbox or any window

except sr.UnknownValueError:
    print("Sorry, I couldn't understand you")
except sr.RequestError as e:
    print(f"Error: {e}")
