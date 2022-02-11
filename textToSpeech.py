import gtts  #api for text to speech conversion
from playsound import playsound  

a = open('fileName.txt', 'r')
# slow = False
t1 = gtts.gTTS(a.read(), slow=False) 

t1.save("welcome.mp3")   
playsound("welcome.mp3")  
