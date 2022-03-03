import speech_recognition as s_r
from langdetect import detect
from googletrans import Translator

print("\nCODE MIXING TRANSLATOR")
print("**********************\n")
print("How do you want to give input:")
print("1.Text\n2.Audio")
n: int = int(input())
if n == 1:
    text = input("Enter the text:\n")  # giving text as input
    print(detect(text))
    if detect(text) == 'te':
        translator = Translator()
        translation = translator.translate(text, src="te", dest="en")
        print(translation)
        translator1 = Translator()
        translation1 = translator1.translate(translation, src="en", dest="hi")
        print(translation1)
    elif detect(text) != 'te':
        translator = Translator()
        translation = translator.translate(text, src='en', dest='te')
        print(translation)
        translator1 = Translator()
        translation1 = translator1.translate(translation, src='te', dest='hi')
        print(translation1)
   else:
        print("Try again")
        exit()
