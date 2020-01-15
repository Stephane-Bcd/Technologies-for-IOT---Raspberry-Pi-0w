
from models import GPIOController
import time

gpc = GPIOController()

print (gpc.test_environment)

gpc.switch_leds_states()


time.sleep(30)

gpc.switch_leds_states(regions_booleans = {
			"Eastern Asia": False,
			"Europe": False,
			"Africa": False,
			"Oceania": False,
			"Northern America": False,
			"South America": False,
			"Western Asia": False
		})
