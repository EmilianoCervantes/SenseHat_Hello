from sense_hat import SenseHat
import time
sense = SenseHat()

r=(255,0,0)
e=(0,0,0)
space=[
	e,e,e,e,e,e,e,e,
	e,r,r,e,r,r,e,e,
	r,r,r,r,r,r,r,e,
	r,r,r,r,r,r,r,e,
	e,r,r,r,r,r,e,e,
	e,e,r,r,r,e,e,e,
	e,e,e,r,e,e,e,e,
	e,e,e,e,e,e,e,e,
]
'''space=[
	e,e,e,r,r,e,e,e,
	e,e,r,r,r,r,e,e,
	e,r,r,r,r,r,r,e,
	r,r,e,r,r,e,r,r,
	r,r,r,r,r,r,r,r,
	e,e,r,e,e,r,e,e,
	e,r,e,r,r,e,r,e,
	r,e,r,e,e,r,e,r,
]'''
sense.set_pixels(space)
sense.set_rotation(180)
