from playsound import playsound
import time
import os
from win10toast import ToastNotifier 
import multiprocessing

timeNeeded = int(input("Input how many seconds timer you need:\n"))
time.sleep(0.5)
vibrate = input("Do you want vibrations?(Y/N):").upper()
ticTac = multiprocessing.Process(target=playsound("SIMPLE TIMER\Tic Tac.mp3", block = False))
ticTac.start()
for i in (range(timeNeeded, -1, -1)):
    os.system("cls")
    print(f"{i:0>2}")
    time.sleep(0.99)
ticTac.kill()

os.system("cls")
display = ToastNotifier()
display.show_toast("Timer!", "The time is up!", threaded=True)  

if vibrate == "Y":
    playsound("SIMPLE TIMER\Vibration.mp3", block = False)
    playsound("SIMPLE TIMER\Alarm beep.mp3")
else:
    playsound("SIMPLE TIMER\Alarm beep.mp3")