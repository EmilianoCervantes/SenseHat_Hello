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

while True:
	temp = round(sense.get_temperature(), 1)
	pres = round(sense.get_pressure(), 1)
	hum = round(sense.get_humidity(), 1)
	
	if temp > 0 and temp < 18.5:
		sense.set_pixels(space)
		sense.set_rotation(270)
	elif temp > 18.5 and temp < 28.7:
		sense.set_pixels(space)
		sense.set_rotation(180)
	elif temp > 28.7 and temp < 31:
		sense.set_pixels(space)
		sense.set_rotation(90)
	else:
		sense.show_message("Humedad: "+str(hum),
			scroll_speed=0.08, back_colour=e)
