import speech_recognition as sr
import pyaudio

def main():
    r = sr.Recognizer()
    r.energy_threshold = 4000
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Say something...")

        audio = r.listen(source )

        try:
            print("You have said \n"+r.recognize_google(audio))

        except Exception as e:
            print("Errot "+ str(e))     

if __name__ == '__main__':
    main()
