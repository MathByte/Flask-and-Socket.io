import serial
from time import *
import numpy as np
'''
def makesure(s):
    s = int(s)
    if s < 10:
        return "00" + str(s)
    if s < 100:
        return "0" + str(s)
    if s < 1000:
        return str(s)
'''

def makesureField(st):
    st = st[2:]

    if len(st) == 1:
        return "0" + st
    if len(st) == 2:
        return st
    
    

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 115200, timeout=5)
    ser.flush()
    s = ""
    ind = 0
    r= 0
    g = 255
    b = 0
    dela = 0.5
    ee = 0
    while True:
        #s = format(ee, 'X')+ format(255 * np.random.random_sample(), 'X') + format(255 * np.random.random_sample(), 'X') + format(255 * np.random.random_sample(), 'X') + '\n'
        #s = makesureField(hex(np.random.randint(0,256))) 
        s = makesureField(hex(ee)) +        makesureField(hex(np.random.randint(0,256))) +        makesureField(hex(np.random.randint(0,256))) +        makesureField(hex(np.random.randint(0,256))) + '\n'
     
        ser.write(s.encode())
        print(s)
        print('\n')
        sleep(dela)
        ee = ee + 1
        if ee == 100:
            ee = 0
            
    #for x in range(100):
     #   s = makesure(x) + makesure(r) + makesure(g) + makesure(b) + '\n'
     #   ser.write(s.encode())
        #print(s.encode())
        
        #ser.write(b"000000000000\n")
        
        
    
    '''
    z = False
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
            z = True
            
        if b == True:
            s = makesure(ee) + makesure(r + ee) + makesure(g) + makesure(b) + '\n'
            ser.write(s.encode())
            ee = ee + 1
            if ee == 100:
                ee = 0
            z = False
    '''
   
'''
import serial
from time import *
import numpy as np

def makesure(s):
    s = int(s)
    if s < 10:
        return "00" + str(s)
    if s < 100:
        return "0" + str(s)
    if s < 1000:
        return str(s)



if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 115200, timeout=5)
    ser.flush()
    s = ""
    ind = 0
    r= 0
    g = 255
    b = 0
    ee = 50
    d = 0.1
    while True:
        
        #s = makesure(ee) + makesure(255 * np.random.random_sample()) + makesure(255 * np.random.random_sample()) + makesure(255 * np.random.random_sample()) + '\n'
        s = makesure(ee) + '000000' + '\n'
        
        ser.write(s.encode())
        print(s)
        print('\n')
        sleep(d)
        s = makesure(ee) + '00FF'+ '\n'
        
        ser.write(s.encode())
        print(s)
        print('\n')
        sleep(d)
        
        s = makesure(ee) + 'FF0000'+ '\n'
        
        ser.write(s.encode())
        print(s)
        print('\n')
        sleep(d)
        
        s = makesure(ee) + '0000FF'+ '\n'
        
        ser.write(s.encode())
        print(s)
        print('\n')
        sleep(d)
            
    #for x in range(100):
     #   s = makesure(x) + makesure(r) + makesure(g) + makesure(b) + '\n'
     #   ser.write(s.encode())
        #print(s.encode())
        
        #ser.write(b"000000000000\n")
        
        
    
    
    z = False
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
            z = True
            
        if b == True:
            s = makesure(ee) + makesure(r + ee) + makesure(g) + makesure(b) + '\n'
            ser.write(s.encode())
            ee = ee + 1
            if ee == 100:
                ee = 0
            z = False
    
   


   


'''

   
