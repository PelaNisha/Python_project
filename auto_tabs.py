import webbrowser, time
url = input("Enter the url: ")
duration = input("Enter the duration: ")
for i in range(2):
    webbrowser.open_new_tab(url)
    time.sleep(int(duration))