import pyttsx3
engine = pyttsx3.init()

while True:
    text_input = input("Enter the text you want to convert to speech (type 'exit' to end): ")
    if text_input.lower() == 'exit':
        break

    engine.say(text_input)
    engine.runAndWait()

engine.stop()
