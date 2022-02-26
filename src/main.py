import speech_recognition as s_r

print("\nCODE MIXING TRANSLATOR")
print("**********************\n")
print("How do you want to give input:")
print("1.Text\n2.Audio")
n = int(input())
if (n == 1):
    text = input("Enter the text:\n")  # giving text as input
elif (n == 2):
    r = s_r.Recognizer()
    my_mic = s_r.Microphone(device_index=1)  # selecting the microphone
    with my_mic as source:
        print("Say now!!!!")
        audio = r.listen(source)  # giving audio as input
    print(r.recognize_google(audio))  # converting audio to text
else:
    print("Try again")
    exit()
