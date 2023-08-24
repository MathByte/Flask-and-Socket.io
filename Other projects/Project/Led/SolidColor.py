

from movingDot import *

class SolidColor:
    def __init__(self, col):
        self.color = col        
    
    def update(self, t):
        pass
   
    
    def draw(self,stripp):
        for x in range(100):
            stripp.setPixelColor(x, self.color)
        
        
