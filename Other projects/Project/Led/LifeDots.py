

from movingDot import *

class LifeDots:
    def __init__(self, many, col):
        self.howMany = many
        self.dots = []
        self.color = col
        self.num = 90
        self.time = 0
        self.val = 2
        self.dots.append(movingDot(0,100 ,0,col,'imortal'))
        #for x in range(1):
            #self.dots.append(movingDot(int(((x+1)/self.num) * 99),20 ,0,col,'imortal'))
       
     
    def update(self, t):
        for x in range(len(self.dots)):
            self.dots[x].update(t)
       
        self.time = self.time + t
        
        if self.time > .2:            
            self.time = 0
            self.dots = []
            for x in range(self.val):
                m = movingDot(int(x * 100/(self.val)), 100, 0, self.color,'imortal')
                self.dots.append(m)
            self.val = self.val + 1
            
            if self.val == 100:
                self.val == 1
                
            
    
    def draw(self,stripp):
        for x in range(len(self.dots)):
            self.dots[x].draw(stripp)
            