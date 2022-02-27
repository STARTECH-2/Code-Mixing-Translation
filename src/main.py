import speech_recognition as s_r
import gtts
from translate import Translator
from langdetect import detect
from playsound import playsound

print("\nCODE MIXING TRANSLATOR")
print("**********************\n")
print("How do you want to give input:")
print("1.Text\n2.Audio")
n: int = int(input())
if n == 1:
    text = input("Enter the text:\n")  # giving text as input
    print(detect(text))
    if detect(text) == 'te':
        translator = Translator(from_lang="telugu", to_lang="english")
        translation = translator.translate(text)
        print(translation)
        translator1 = Translator(from_lang="english", to_lang="hindi")
        translation1 = translator1.translate(translation)
        print(translation1)
        # make request to google to get synthesis
        tts = gtts.gTTS(translation1, lang="hi")
        # save the audio file
        tts.save("my-translation.mp3")
        # play the audio file
        playsound("my-translation.mp3")
    elif detect(text) == 'en':
        translator = Translator(from_lang="english", to_lang="telugu")
        translation = translator.translate(text)
        print(translation)
        translator1 = Translator(from_lang="telugu", to_lang="hindi")
        translation1 = translator1.translate(translation)
        print(translation1)
        # make request to google to get synthesis
        tts = gtts.gTTS(translation1, lang="hi")
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
    print(r.recognize_google(audio))  # converting audio to text
    text1 = r.recognize_google(audio)
    print(detect(text1))
    if detect(text1) == 'te':
        translator = Translator(from_lang="telugu", to_lang="english")
        translation = translator.translate(text1)
        print(translation)
        translator1 = Translator(from_lang="english", to_lang="hindi")
        translation1 = translator1.translate(translation)
        print(translation1)
        # make request to google to get synthesis
        tts = gtts.gTTS(translation1, lang="hi")
        # save the audio file
        tts.save("my-translation.mp3")
        # play the audio file
        playsound("my-translation.mp3")
    elif detect(text1) == 'en':
        translator = Translator(from_lang="english", to_lang="telugu")
        translation = translator.translate(text1)
        print(translation)
        translator1 = Translator(from_lang="telugu", to_lang="hindi")
        translation1 = translator1.translate(translation)
        print(translation1)
        # make request to google to get synthesis
        tts = gtts.gTTS(translation1, lang="hi")
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
