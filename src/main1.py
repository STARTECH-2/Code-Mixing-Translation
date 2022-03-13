import speech_recognition as s_r
import gtts
# from translate import Translator
from langdetect import detect
from playsound import playsound
from googletrans import Translator
import pytesseract
from PIL import Image
# import pyttsx3
# from scipy.io import wavfile

print("\nCODE MIXING TRANSLATOR")
print("**********************\n")
print("How do you want to give input:")
print("1.Text\n2.Audio\n3.File\n4.Image")
n: int = int(input())
if n == 1:
    text = input("Enter the text:\n")  # giving text as input
    print(detect(text))
    if detect(text) == 'te':
        translator = Translator()
        translation = translator.translate(text, src='te', dest='en')
        print(translation.text)
        translator1 = Translator()
        translation1 = translator1.translate(translation.text, src='en', dest='hi')
        print(translation1.text)
        # make request to google to get synthesis
        tts = gtts.gTTS(translation1.text, lang="hi")
        # save the audio file
        tts.save("my-translation.mp3")
        # play the audio file
        playsound("my-translation.mp3")
    elif detect(text) != 'te':
        translator = Translator()
        translation = translator.translate(text, src='en', dest='te')
        print(translation.text)
        translator1 = Translator()
        translation1 = translator1.translate(translation.text, src='te', dest='hi')
        print(translation1.text)
        # make request to google to get synthesis
        tts = gtts.gTTS(translation1.text, lang="hi")
        # save the audio file
        tts.save("my-translation.mp3")
        # play the audio file
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
    print(detect(text1))
    if detect(text1) == 'te':
        translator = Translator()
        translation = translator.translate(text1, src='te', dest='en')
        print(translation.text)
        translator1 = Translator()
        translation1 = translator1.translate(translation.text, src='en', dest='hi')
        print(translation1.text)
        # make request to google to get synthesis
        tts = gtts.gTTS(translation1.text, lang="hi")
        # save the audio file
        tts.save("my-translation.mp3")
        # play the audio file
        playsound("my-translation.mp3")
    elif detect(text1) != 'te':
        translator = Translator()
        translation = translator.translate(text1, src='en', dest='te')
        print(translation.text)
        translator1 = Translator()
        translation1 = translator1.translate(translation.text, src='te', dest='hi')
        print(translation1.text)
        # make request to google to get synthesis
        tts = gtts.gTTS(translation1.text, lang="hi")
        # save the audio file
        tts.save("my-translation.mp3")
        # play the audio file
        playsound("my-translation.mp3")
    else:
        print("Try again")
        exit()
elif n == 3:
    filename = 'G:/PPT/2 - 2/AI DS/Project/Code-Mixing Translation DataSet/Voice 100.wav '
    r = s_r.Recognizer()
    with s_r.AudioFile(filename) as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        text2 = r.recognize_google(audio_data)
        print(text2)
        print(detect(text2))
        if detect(text2) == 'te':
            translator = Translator()
            translation = translator.translate(text2, src='te', dest='en')
            print(translation.text)
            translator1 = Translator()
            translation1 = translator1.translate(translation.text, src='en', dest='hi')
            print(translation1.text)
            # make request to google to get synthesis
            tts = gtts.gTTS(translation1.text, lang="hi")
            # save the audio file
            tts.save("my-translation.mp3")
            # play the audio file
            playsound("my-translation.mp3")
        elif detect(text2) != 'te':
            translator = Translator()
            translation = translator.translate(text2, src='en', dest='te')
            print(translation.text)
            translator1 = Translator()
            translation1 = translator1.translate(translation.text, src='te', dest='hi')
            print(translation1.text)
            # make request to google to get synthesis
            tts = gtts.gTTS(translation1.text, lang="hi")
            # save the audio file
            tts.save("my-translation.mp3")
            # play the audio file
            playsound("my-translation.mp3")
        else:
            print("Try again")
            exit()
elif n == 4:
    img = Image.open('G:/PPT/2 - 2/AI DS/Project/Code-Mixing Translation DataSet/Image Dataset/text1.png')
    print(img)
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
    text3 = pytesseract.image_to_string(img)
    # write text in a text file and save it to source path
    with open('abc.txt', mode='w') as file:
        file.write(text3)
        print(text3)
    print(detect(text3))
    if detect(text3) == 'te':
        translator = Translator()
        translation = translator.translate(text3, src='te', dest='en')
        print(translation.text)
        translator1 = Translator()
        translation1 = translator1.translate(translation.text, src='en', dest='hi')
        print(translation1.text)
        # make request to google to get synthesis
        tts = gtts.gTTS(translation1.text, lang="hi")
        # save the audio file
        tts.save("my-translation.mp3")
        # play the audio file
        playsound("my-translation.mp3")
    elif detect(text3) != 'te':
        translator = Translator()
        translation = translator.translate(text3, src='en', dest='te')
        print(translation.text)
        translator1 = Translator()
        translation1 = translator1.translate(translation.text, src='te', dest='hi')
        print(translation1.text)
        # make request to google to get synthesis
        tts = gtts.gTTS(translation1.text, lang="hi")
        # save the audio file
        tts.save("my-translation.mp3")
        # play the audio file
        playsound("my-translation.mp3")
    else:
        print("Try again")
        exit()
else:
    print("Try again")
    exit()
