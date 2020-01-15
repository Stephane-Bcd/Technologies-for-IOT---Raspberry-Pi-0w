
from models import GPIOController

gpc = GPIOController()

print (gpc.test_environment)

gpc.switch_leds_states()
