import mss
import time
import pyautogui
import winsound
import keyboard

blue = [(54, 159, 198)]
black = [(0, 0, 0), (16,20,19)]
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 100  # Set Duration To 1000 ms == 1 second
searchFor = blue
time.sleep(1)
winsound.Beep(frequency,duration)
sct = mss.mss()
monitor = {"top": 37, "left": 663, "width": 600, "height": 990}
footer = 250

while True:

    if keyboard.is_pressed('q'):
        break
    # Get a screen shot
    sct_img = sct.grab(monitor)
    if searchFor == blue:
        searchHeight = sct_img.height - footer
    else:
        searchHeight = sct_img.height

    for i in reversed(range(0 + 100,searchHeight)):
        # first column
        if sct_img.pixel(75,i) in searchFor:
            pyautogui.click(75 + 663, i + 37 )
            print("click")
            searchFor = black
            break

        # second column
        elif sct_img.pixel(225,i) in searchFor:
            pyautogui.click(225 + 663, i + 37)
            print("click")
            searchFor = black
            break

        elif sct_img.pixel(375,i) in searchFor:
            pyautogui.click(375 + 663, i + 37 )
            print("click")
            searchFor = black
            break

        elif sct_img.pixel(525,i) in searchFor:
            pyautogui.click(525 + 663, i + 37 )
            print("click")
            searchFor = black
            break

