import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Define a function to perform speech recognition
def recognize_speech():
    with sr.Microphone() as source:
        print("Speak something...")
        audio = recognizer.listen(source)

    try:
        # Use Google Speech Recognition to convert speech to text
        text = recognizer.recognize_google(audio)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Call the function to perform speech recognition
recognize_speech()
