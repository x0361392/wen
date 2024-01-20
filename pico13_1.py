from machine import Pin
import time

red_led = Pin(15,mode=Pin.OUT)
btn = Pin(14,mode=Pin.PULL_DOWN)
is_press=false

while True:
    if btn.value():
       is_press = true
    else is_preaa:
        pprint('releasa')
        is_press = false