import speech_recognition as sr
from datetime import datetime
from PySide6.QtCore import QDate


def recognize_speech():
  recognizer = sr.Recognizer()
  with sr.Microphone() as source:
    print("Speak the date...")
    audio = recognizer.listen(source)

  try:
    text = recognizer.recognize_google(audio)
    print("You said:", text)
    return text
  except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
  except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))


# Get the spoken date
spoken_date = recognize_speech()

# Define possible date formats (adjust as needed)
formats = ["%dth %B %Y", "%B %d, %Y", "%B %dth %Y", "%B %d %Y"]  # Add more formats if users might use variations

for format_str in formats:
  try:
    # Try parsing the spoken date with each format
    desired_date = datetime.strptime(spoken_date, format_str)
    break  # Exit the loop if parsing is successful
  except ValueError:
    pass  # If parsing fails with this format, try the next one

if desired_date:  # Check if parsing was successful with any format
  # Convert datetime to QDate and set the calendar date (as before)
  qt_date = QDate(desired_date.year, desired_date.month, desired_date.day)
  print(f"Setting the date to {qt_date.toString()}")
else:
  print("Sorry, I couldn't understand the date format. Please try again.")
