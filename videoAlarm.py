import webbrowser
import time

interval = int(input("enter break intetrval: "))
for i in range(int(input("enter no. of break needed: "))):
    time.sleep(interval*60)
    webbrowser.open("https://www.youtube.com/watch?v=g-ezvnq8Jww")
