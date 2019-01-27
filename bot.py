import mss
import pyautogui as cursor
import keyboard
import time

blue = [(54, 159, 198)]
black = [(0, 0, 0), (16,20,19)]
searchFor = blue

time.sleep(1)
sct = mss.mss()
screenDimensions = {"top": 37, "left": 663, "width": 600, "height": 990}
footer = 250

while True:
    if keyboard.is_pressed('q'): # Emergency Button
        break
    # Get a screen shot
    sct_img = sct.grab(screenDimensions)
    if searchFor == blue:
        searchHeight = sct_img.height - footer
    else:
        searchHeight = sct_img.height

    for i in reversed(range(0 ,searchHeight)):
        # first column
        if sct_img.pixel(75,i) in searchFor:
            if i>88: # To prevent pop ups
                cursor.click(75 + 663, i + 37 )
            searchFor = black
            break

        # second column
        elif sct_img.pixel(225,i) in searchFor:
            cursor.click(225 + 663, i + 37)
            searchFor = black
            break

        elif sct_img.pixel(375,i) in searchFor:
            cursor.click(375 + 663, i + 37 )
            searchFor = black
            break

        elif sct_img.pixel(525,i) in searchFor:
            cursor.click(525 + 663, i + 37 )
            searchFor = black
            break

