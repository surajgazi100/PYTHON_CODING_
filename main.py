import speech_recognition as sr
r = sr.Recognizer()
with sr.AudioFile('steveJobsSpeech_2min.wav') as source:
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print('working on...')
    except :
        print('sorry')