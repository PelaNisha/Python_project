# Python program that takes a url and duration, opens the url in different tabs after a certain duration
# Uses: Can be used to increase view of a youtube video

import webbrowser, time
url = input("Enter the url: ")
duration = input("Enter the duration: ")
for i in range(2):                      # here 2 is the number of tabs we want to open
    webbrowser.open_new_tab(url)
    time.sleep(int(duration))           # time in between we open the next tab
