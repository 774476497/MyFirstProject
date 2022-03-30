import speech_recognition as sr
import pyttsx3 
  
    #   تحويل النص الى صوت                   
def speaktext(command):
    engine=pyttsx3.init()
    engine.say(command)
    engine.runAndwait()

 #    تحويل الصوت الى نص وحفظه الى ملف #      
so = sr.Recognizer()
with sr.Microphone() as mic:
    print("say something...")
    so.adjust_for_ambient_noise(mic, duration=1)
    myaudio=so.listen(mic) 
    mytext=so.recognize_google(myaudio)
    mytext=mytext.lower()
   
    print(mytext)
    f = open('path file' , 'a')
    f.writelines(w)
    f.close()
  
speaktext(w)
 
