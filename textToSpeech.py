import gtts  
from playsound import playsound  

a = open('botalk.txt', 'r')
# slow = False
t1 = gtts.gTTS(a.read(), slow=False) 

t1.save("welcome.mp3")   
playsound("welcome.mp3")  