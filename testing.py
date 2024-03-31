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

# import editdistance 

# def find_similar_words(word, word_list):
#     if len(word) < 3:
#         max_distance = 0
#     else:
#         max_distance = 2
#     similar_words = []
#     for candidate in word_list:
#         distance = editdistance.eval(word, candidate)
#         if distance <= max_distance:
#             similar_words.append(candidate)
#         elif all(char in candidate for char in word):
#             similar_words.append(candidate)
#     # Sort by distance (ascending order)
#     similar_words.sort(key=lambda x: editdistance.eval(word, x))  # Sort directly using editdistance
#     return similar_words

# # Example usage
# word = "ha"
# word_list = ["sad", "angry", "joyful", "glad", "happiness", "happier", "happiest", "happily", "happy"]
# similar_words = find_similar_words(word, word_list)
# print(f"Similar words for '{word}' (sorted by distance): {similar_words}")
