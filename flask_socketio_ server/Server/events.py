from flask import request
from flask_socketio import emit
from time import sleep
from threading import Thread
from .extensions import socketio
import time
import board
import neopixel
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 100
ORDER = neopixel.RGB


pixels = neopixel.NeoPixel(        pixel_pin, num_pixels, brightness=1, auto_write=False, pixel_order=ORDER    )
# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.


def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (b, r, g) ##(r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)
    print("done")



def clear_leds():
    pixels.fill((0, 0, 0))
    pixels.show()

def move_group(position, group_size, colorr):
    clear_leds()
    if position + group_size > 100:
        for i in range(position, 100):
            pixels[i] = colorr  # Set RGB color (red) for the group
        for i in range(0, position + group_size - 100):
            pixels[i] = colorr  # Set RGB color (red) for the group
    else:
        for i in range(position, position + group_size):
            pixels[i] = colorr  # Set RGB color (red) for the group
    pixels.show()



def FillFromLeft(s, l, r):
   
    for i in range(num_pixels):
        if i == 0:
            pixels[i] = (0, 20, 0)
            continue
        if i > 0:
            if l != 1:
                for y in range(l):
                    pixels[i - y] = (0, 20, 0)        
        pixels[i] = (0, 0, 0)
        
    pixels.show()
    time.sleep(wait)
    print("done")


    
def hex_to_rgb(hex_string):
    hex_string = hex_string.lstrip('#')
    if len(hex_string) != 6:
        raise ValueError("Invalid hexadecimal color string")
    r = int(hex_string[0:2], 16)
    g = int(hex_string[2:4], 16)
    b = int(hex_string[4:6], 16)
    return b, r, g

def setColor(co):
    print(hex_to_rgb(co))
    pixels.fill(hex_to_rgb(co))    
    pixels.show()
    return hex_to_rgb(co)
        
def setColorRGB(co):
    print(AdjustRange(co))
    pixels.fill(AdjustRange(co))    
    pixels.show()
    return AdjustRange(co)

def AdjustRange(co):
    rgb = co.lstrip('!')
    rgbArray = rgb.split(' ')
    rgbArray = [int(int(x) * 12.75)for x in rgbArray]     
    return rgbArray[2], rgbArray[0], rgbArray[1]




done = False


def fire(S, L, R, co):
    global done
    if R == 0:
        print("once inside thread")
        #for i in range(0, 100 - L + 1):
        for i in range(0, 101):
            move_group(i, L, co)
            if S != 0:
                time.sleep(S * 0.005)
            else:
                break

    else:
        print("while not done inside thread")
        while not done:
            for i in range(101 - L + 1):
                move_group(i, L, co)
                if S != 0:
                    time.sleep(S * 0.005)
                else:
                    break
        print("while exited")

def shoot(co):
    global done
    slr = co.lstrip('@')
    slr = slr.split(' ')

    print(slr)
    if len(slr) == 1:
        done = True
        print("done = true")
    else:
        done = False
        S = int(slr[0])
        L = int(slr[1])
        R = 0 if (slr[2] == 'false') else 1
        co = hex_to_rgb(slr[3])
        thread = Thread(target=fire, args=(S, L, R, co))
        thread.start()
        print("thread started and program continued")

        



    #rainbow_cycle(.0004)
    #pixels.fill(AdjustRange(co))    
    #pixels.show()
    return "shoot is finished"


def retractFromBothSides(S, M, co):
    pixels.fill(co)
    pixels.show()

    for x in range(50):
        pixels[x] = (0,0,0)
        pixels[99 - x] = (0,0,0)
        pixels.show()
        if S + 60 * M != 0:
            time.sleep( (S / 50))
            print( (S / 50))

def increaseToBothSides(S, M, co):
    pixels.fill((0, 0, 0))
    pixels.show()

    for x in range(50):
        pixels[50 - x - 1] = co
        pixels[50 + x] = co
        pixels.show()
        if S + 60 * M != 0:
            time.sleep( (S / 50))
            print( (S / 50))

def setTimerCount(co):
    global done
    slr = co.lstrip('$')
    slr = slr.split(' ')

    print(slr)
 
    done = False
    if slr[0] == 'D':
        S = int(slr[1])
        M = int(slr[2])  
        co = hex_to_rgb(slr[3])

        thread = Thread(target=retractFromBothSides, args=(S, M, co,))
        thread.start()
    else:
        S = int(slr[1])
        M = int(slr[2])  
        co = hex_to_rgb(slr[3])

        thread = Thread(target=increaseToBothSides, args=(S, M, co,))
        thread.start()
    print("thread started and program continued")
    return "timer is finished"
#-----------------------------------------------------------------------------------------------------------------------------------


users = {}

@socketio.on("connect")
def handle_connect():
    print("Client connected!")

@socketio.on("user_join")
def handle_user_join(username):
    print(f"User {username} joined!")
    users[username] = request.sid

@socketio.on("new_message")
def handle_new_message(message):
    print(f"New message: {message}")

    if message[0] =='#':
        message = setColor(message)
    
    if message[0] =='!':
        message = setColorRGB(message)

    if message[0] =='@':
        message = shoot(message)

    if message[0] =='$':
        message = setTimerCount(message)

    username = None 
    for user in users:
        if users[user] == request.sid:
            username = user
    emit("chat", {"message": message, "username": username}, broadcast=True)




