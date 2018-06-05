from sense_hat import SenseHat
import time
sense = SenseHat()

ang = [0,90,180,270,0,90,180,270]
i=0
while True:
	sense.show_message("Hello")
	time.sleep(0.5)
	sense.set_rotation(ang[i])
	if i <8:
		i+=1
