from sense_hat import SenseHat
import time
sense = SenseHat()

r=(255,0,0)
e=(0,0,0)

space=[
	e,e,e,r,r,e,e,e,
	e,e,r,r,r,r,e,e,
	e,r,r,r,r,r,r,e,
	r,r,e,r,r,e,r,r,
	r,r,r,r,r,r,r,r,
	e,e,r,e,e,r,e,e,
	e,r,e,r,r,e,r,e,
	r,e,r,e,e,r,e,r,
]

def rojo():
	sense.clear(255,0,0)
def azul():
	sense.clear(0,0,255)
	
def temp():
	temp = round(sense.get_temperature(), 1)
	if temp < 18:
		sense.show_message("Temperatura: "+str(temp),
			scroll_speed=0.08, text_colour=[0,0,255], back_colour=e)
	elif temp > 26.5:
		sense.show_message("Temperatura: "+str(temp),
			scroll_speed=0.08, text_colour=[255,0,0], back_colour=e)
	else:
		sense.show_message("Temperatura: "+str(temp),
			scroll_speed=0.08, text_colour=[0,0,0], back_colour=e)

def hum():
	hum = round(sense.get_humidity(), 1)
	sense.show_message("Humedad: "+str(hum),
			scroll_speed=0.08, back_colour=e)
	sense.set_pixels(space)
	sense.set_rotation(180)

def press():
	pres = round(sense.get_pressure(), 1)
	sense.show_message("Presion: "+str(press),
			scroll_speed=0.08, back_colour=e)

sense.stick.direction_left=temp
sense.stick.direction_right=hum
#sense.stick.direction_middle
sense.stick.direction_up=press
#sense.stick.direction_down=verde

while 1:
	pass
	
