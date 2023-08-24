import serial
from time import *
import numpy as np

    

if __name__ == '__main__':
    
    ser = serial.Serial('/dev/ttyAMA0', 115200, timeout=1)
    ser.open()

    ser.write("testing")
    try:
        
        while 1:
            response = ser.readline()
            print (response)
    except KeyboardInterrupt:
        ser.close()
