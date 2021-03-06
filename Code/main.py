import speech_recognition as s_r
import gtts
from langdetect import detect
from playsound import playsound
from googletrans import Translator
from PIL import Image
import pytesseract

print("\nCODE MIXING TRANSLATOR")
print("**********************\n")
print("How do you want to give input:")
print("1.Text\n2.Audio\n3.File\n4.Image")
n: int = int(input())
if n == 1:
    text = input("Enter the text:\n")
    if detect(text) == 'te':
        translator = Translator()
        translation = translator.translate(text, src='te', dest='en')
        # print(translation.text)
        translator1 = Translator()
        translation1 = translator1.translate(translation.text, src='en', dest='hi')
        print(translation1.text)
        tts = gtts.gTTS(translation1.text, lang="hi")
        tts.save("my-translation.mp3")
        playsound("my-translation.mp3")
    elif detect(text) != 'te':
        translator = Translator()
        translation = translator.translate(text, src='en', dest='te')
        # print(translation.text)
        translator1 = Translator()
        translation1 = translator1.translate(translation.text, src='te', dest='hi')
        print(translation1.text)
        tts = gtts.gTTS(translation1.text, lang="hi")
        tts.save("my-translation.mp3")
        playsound("my-translation.mp3")
    else:
        print("Try again")
        exit()
elif n == 2:
    r = s_r.Recognizer()
    my_mic = s_r.Microphone(device_index=1)  # selecting the microphone
    with my_mic as source:
        print("Say now!!!!")
        audio = r.listen(source)  # giving audio as input
        captured_audio = r.record(source=my_mic, duration=3)
    print(r.recognize_google(audio))  # converting audio to text
    text1 = r.recognize_google(audio)
    if detect(text1) == 'te':
        translator = Translator()
        translation = translator.translate(text1, src='te', dest='en')
        # print(translation.text)
        translator1 = Translator()
        translation1 = translator1.translate(translation.text, src='en', dest='hi')
        print(translation1.text)
        tts = gtts.gTTS(translation1.text, lang="hi")
        tts.save("my-translation.mp3")
        playsound("my-translation.mp3")
    elif detect(text1) != 'te':
        translator = Translator()
        translation = translator.translate(text1, src='en', dest='te')
        # print(translation.text)
        translator1 = Translator()
        translation1 = translator1.translate(translation.text, src='te', dest='hi')
        print(translation1.text)
        tts = gtts.gTTS(translation1.text, lang="hi")
        tts.save("my-translation.mp3")
        playsound("my-translation.mp3")
    else:
        print("Try again")
        exit()
elif n == 3:
    filename = ' # GIVE PATH OF YOUR WAV FILE '
    r = s_r.Recognizer()
    with s_r.AudioFile(filename) as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        text2 = r.recognize_google(audio_data)
        print(text2)
        if detect(text2) == 'te':
            translator = Translator()
            translation = translator.translate(text2, src='te', dest='en')
            # print(translation.text)
            translator1 = Translator()
            translation1 = translator1.translate(translation.text, src='en', dest='hi')
            print(translation1.text)
            tts = gtts.gTTS(translation1.text, lang="hi")
            tts.save("my-translation.mp3")
            playsound("my-translation.mp3")
        elif detect(text2) != 'te':
            translator = Translator()
            translation = translator.translate(text2, src='en', dest='te')
            # print(translation.text)
            translator1 = Translator()
            translation1 = translator1.translate(translation.text, src='te', dest='hi')
            print(translation1.text)
            tts = gtts.gTTS(translation1.text, lang="hi")
            tts.save("my-translation.mp3")
            playsound("my-translation.mp3")
        else:
            print("Try again")
            exit()
elif n == 4:
    img = Image.open(' GIVE PATH OF YOUR IMAGE FILE ')
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
    text3 = pytesseract.image_to_string(img)
    with open('abc.txt', mode='w') as file:
        file.write(text3)
        print(text3)
    # write text in a text file and save it to source path
    # print(detect(text3))
    if detect(text3) == 'te':
        translator = Translator()
        translation = translator.translate(text3, src='te', dest='en')
        # print(translation.text)
        translator1 = Translator()
        translation1 = translator1.translate(translation.text, src='en', dest='hi')
        print(translation1.text)
        tts = gtts.gTTS(translation1.text, lang="hi")
        tts.save("my-translation.mp3")
        playsound("my-translation.mp3")
    elif detect(text3) != 'te':
        translator = Translator()
        translation = translator.translate(text3, src='en', dest='te')
        # print(translation.text)
        translator1 = Translator()
        translation1 = translator1.translate(translation.text, src='te', dest='hi')
        print(translation1.text)
        tts = gtts.gTTS(translation1.text, lang="hi")
        tts.save("my-translation.mp3")
        playsound("my-translation.mp3")
    else:
        print("Try again")
        exit()
else:
    print("Try again")
    exit()
