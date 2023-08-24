
from LifeDots import *
from rpi_ws281x import *
from movingDot import *
from SolidColor import *
from LifeDots import *
from Fixedblock import *

# LED strip configuration:
LED_COUNT      = 100      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53





class engin:
    def __init__(self, diss):
        self.allcolors = [Color(0,0,0) for ii in range(100)]
        self.dis = diss
        # Create NeoPixel object with appropriate configuration.
        self.strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
        self.strip.setBrightness(255)
        # Intialize the library (must be called once before other functions).
        self.strip.begin()
        self.creatures = []
        self.stopitforasec = False
        #self.creatures = [movingDot(0,-500,0, Color(255,255,255)),movingDot(0,-300,0, Color(255,0,255)),movingDot(0,200,0, Color(255,255,0)), movingDot(0,100,0, Color(255,0,0)),movingDot(0,-100,0, Color(0,255,0))]
        
        #self.creatures.append(movingDot(0,10,0, Color(255,0,0)))
        #self.creatures.append(fixedBlock(50,50,Color(255,0,0)))
        #self.creatures.append(SolidColor(Color(255,0,0)))
       
    def draw(self):
        if self.stopitforasec != True:
            for i in range(self.strip.numPixels()):
                self.strip.setPixelColor(i, Color(0,0,0))
            
            for c in self.creatures:
                c.draw(self.strip)
            
            
            self.strip.show()
        
        
    def update(self, t):
        if self.stopitforasec != True:
            try:
                for c in self.creatures:
                    c.update(t)
                if c.died == True:
                    self.creatures.remove(c)
                    #print('removed')
            except:
                pass
                #print(c.died)
            
                
                
                        
                
 
    def setsolidColor(self, co):
        self.stopitforasec = True
        self.creatures = []
        self.creatures.append(SolidColor(co))
        self.stopitforasec = False
        
        
    def addAnim(self,an):
        self.stopitforasec = True
        time.sleep(0.1)
        self.creatures.append(an)
        self.stopitforasec = False
    
    def startFixedAnimation(self,v):
        self.stopitforasec = True
        time.sleep(0.1)
        self.creatures = []
        self.creatures.append(v)
        self.stopitforasec = False
       
    def animTosolid(self,m,colo):
        self.stopitforasec = True
        time.sleep(0.1)
        self.creatures = []
        self.creatures.append(LifeDots(m,colo))
        self.stopitforasec = False
                    
