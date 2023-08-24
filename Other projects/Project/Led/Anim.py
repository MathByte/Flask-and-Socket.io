
import random
from rpi_ws281x import *

class Aminamtion:
    def __init__(self, namee, wait = 50,iteration=5, colorr = Color(0,255,0)):
        self.name = namee
        self.wait_ms = wait
        self.pixels = [Color(0,0,0) for x in range(100)]
        self.time = 0
        self.j = 0
        self.i = 0
        self.q = 0
        self.b = 0
        self.iterations = iteration
        self.color = colorr
   
    def update(self, t):
      
        if self.name == 'theaterChaseRainbow':
            
            self.time = self.time + 0.016
           
            
            if int(self.time * 1000) > self.wait_ms:
                self.time = 0
                if self.b == 1:
                    self.b = 0
                else:
                    self.b = 1
                    
            
            if self.b == 1:
                for x in range(0,100):
                    self.pixels[x] = self.wheel(((x+self.j) % 255))
                
            else:
                for x in range(0,100):
                    self.pixels[x] = 0
            
          
            if self.j <= 254:
                self.j = self.j + 1
            else:
                self.j = 0
                
            
            
        if self.name == 'rainbowCycle':
            """Draw rainbow that uniformly distributes itself across all pixels."""
            self.time = self.time + 0.016
           
            
            if int(self.time * 1000) > self.wait_ms:
                self.time = 0
                if self.b == 1:
                    self.b = 0
                else:
                    self.b = 1
          
            
            if self.b == 1:
                for x in range(0,100):
                    self.pixels[x] = self.wheel((int(x * 256 / 100) + self.j) & 255)
                
            else:
                for x in range(0,100):
                    self.pixels[x] = self.wheel((int(x * 256 / 100) + self.j) & 255)
            
           
            self.j = self.j + 1
            if 256*self.iterations < self.j:
                self.j = 0
            
          
            
            
            
            '''
              for j in range(256*iterations):
                for i in range(strip.numPixels()):
                    strip.setPixelColor(i, self.wheel((int(i * 256 / strip.numPixels()) + j) & 255))
                strip.show()
                time.sleep(wait_ms/1000.0)
                
                
                
                
            for j in range(256):
                for q in range(3):
                    for i in range(0, 100, 3):
                        print(i,j)
                        self.pixels[i+q] = wheel(((i+j) % 255))
                    #strip.show()
                    time.sleep(self.wait_ms/1000.0)
                    for i in range(0, 100, 3):
                        self.pixels[i+q] = 0
                        #print(i,j)
            '''
        if self.name == 'rainbow':
            """Draw rainbow that uniformly distributes itself across all pixels."""
            self.time = self.time + 0.016
           
            
            if int(self.time * 1000) > self.wait_ms:
                self.time = 0
                if self.b == 1:
                    self.b = 0
                else:
                    self.b = 1
          
            
            if self.b == 1:
                for x in range(0,100):
                    self.pixels[x] = self.wheel((x+self.j) & 255)
                
            else:
                for x in range(0,100):
                    self.pixels[x] = self.wheel((x+self.j) & 255)            
           
            self.j = self.j + 1
            if 256*self.iterations < self.j:
                self.j = 0
            
          
        if self.name == 'colorWipe':
            """Wipe color across display a pixel at a time."""
            
            self.time = self.time + 0.016
           
            
            if int(self.time * 1000) > self.wait_ms:
                self.time = 0
                self.pixels[self.i] = self.color
                self.i = self.i + 1
                if self.i == 100:
                    self.i = 0
                    self.color = Color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
               
          
            
           
            
            

    
    def draw(self,stripp):
        for x in range(100):
            stripp.setPixelColor(x, self.pixels[x])
        
    def wheel(self,pos):
        """Generate rainbow colors across 0-255 positions."""
        if pos < 85:
            return Color(pos * 3, 255 - pos * 3, 0)
        elif pos < 170:
            pos -= 85
            return Color(255 - pos * 3, 0, pos * 3)
        else:
            pos -= 170
            return Color(0, pos * 3, 255 - pos * 3)

    
