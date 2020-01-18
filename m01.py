from microbit import *

while True:
    display.scroll('Hello Paul!')
    display.show(Image.DIAMOND)
    sleep(2000)
    display.show(Image.TORTOISE)
    sleep(1000)