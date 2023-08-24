

class fixedBlock:
    def __init__(self, pos, widthh, col):
        self.width = widthh
        self.pos = []
        self.color = col
        self.died = False
        if pos - widthh >= 0 and pos + widthh <= 99:
            for x in range(pos - widthh, pos + widthh):
                self.pos.append(x)
        else:
            if pos - widthh < 0 and pos + widthh <= 99:
                for x in range(0, pos + widthh):
                    self.pos.append(x)
            else:
                if pos - widthh >= 0 and pos + widthh > 99:
                    for x in range(pos - widthh, 100):
                        self.pos.append(x)
                
            
       
        
        
    def update(self, t):
        pass
        
    
            
    def draw(self,stripp):
        for x in range(len(self.pos)):
            stripp.setPixelColor(self.pos[x], self.color)
      
        
