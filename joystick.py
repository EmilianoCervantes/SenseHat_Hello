from sense_hat import SenseHat
import time
sense = SenseHat()

def rojo():
	sense.clear(255,0,0)
def azul():
	sense.clear(0,0,255)
def amarillo():
	sense.clear(0,255,0)
def verde():
	sense.clear(0,255,255)

sense.stick.direction_left=azul
sense.stick.direction_right=rojo
sense.stick.direction_middle=sense.clear
sense.stick.direction_up=amarillo
sense.stick.direction_down=verde

while 1:
	pass


