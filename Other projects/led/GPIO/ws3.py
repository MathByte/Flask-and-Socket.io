import board
import neopixel

from time import sleep



pixels = neopixel.NeoPixel(board.D18, 100)


pixels.fill((0, 0, 0))

pixels.show()
sleep(1)

pixels.fill((255, 255, 255))

pixels.show()
sleep(1)

pixels.fill((0, 0, 0))

pixels.show()
sleep(1)