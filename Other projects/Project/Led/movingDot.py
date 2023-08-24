import time

class movingDot:
    def __init__(self, posee, initspeed, initacc, col,mortal):
        self.initspeed = initspeed
        self.initpos = posee
        self.pos = 0
        self.initacc = initacc
        self.color = col
        self.time = 0
        self.imortal = mortal
        self.died = False
        self.rotationsCount = 0
        self.actualPoss = 0
       
        
        
    def update(self, t):
        if self.imortal == 'imortal':
            
            #time.sleep(0.1)
            if self.initacc == 0:
                self.pos = self.time * self.initspeed + self.initpos
            else:
                self.pos = 0.5 * self.time * self.time * self.initacc + self.time * self.initspeed + self.initpos
            
            self.time = self.time + t
            self.actualPoss = self.pos
            
            self.pos = int(round(self.pos))
            self.pos = self.pos % 100
            if self.pos < 0:
                self.pos = 100 + self.pos
            if self.time > 60:
                self.time = 0
    
            d = self.actualPoss / 100
            r = self.actualPoss % 100
            #print(d, r)
            #print(self.actualPoss)
            
          
        else:
            if self.imortal == 'not':
                if self.died == False:
                    if self.initacc == 0:
                        self.pos = self.time * self.initspeed
                    else:
                        self.pos = 0.5 * self.time * self.time * self.initacc + self.time * self.initspeed
                                    
                    self.time = self.time + t
                    self.pos = int(round(self.pos))
                    
                    if self.pos > 99:
                        self.died = True
                        
                    if self.pos < 0:
                        self.died = True
                       
                    
                
    
            
    def draw(self, stripp):
        stripp.setPixelColor(self.pos, self.color)
        
