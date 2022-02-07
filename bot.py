import pyttsx3
engine = pyttsx3.init()                    #printing current voice rate
engine.setProperty('rate', 180)                           #printing current volume level
engine.setProperty('volume',0.5) 

voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[14].id) #changing index, changes voices. o for male and 1 for female

engine.say("Happy rose day neisa, i miss you")
engine.runAndWait()
engine.stop()