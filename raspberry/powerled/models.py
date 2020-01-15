try:
	import RPi.GPIO as GPIO #Importe la bibliothèque pour contrôler les GPIOs
	test_environment = False
except (ImportError, RuntimeError):
	test_environment = True

import time

class GPIOController:
	
	def __init__(self):
		self.test_environment = test_environment
		self.regions_leds = {
			"Eastern Asia": 5,
			"Europe": 2,
			"Africa": 3,
			"Oceania": 6,
			"Northern America": 7,
			"South America": 0,
			"Western Asia": 4
		}
		self.regions_leds_states = {}
		
		if not test_environment:
			#Définit le mode de numérotation (Board)
			GPIO.setmode(GPIO.BOARD) 
			#On désactive les messages d'alerte
			GPIO.setwarnings(False) 
			
			#Active le contrôle du GPIO
			for region in self.regions_leds:
				GPIO.setup(self.regions_leds[region], GPIO.OUT)
			
			self.read_state()

	def read_state(self):
		
		#Lit l'état actuel du GPIO, vrai si allumé, faux si éteint
		if not test_environment:
			for region in self.regions_leds:
				self.regions_leds_states[region] = GPIO.input(self.regions_leds[region])
				
	def switch_leds_states(self, regions_booleans = {
			"Eastern Asia": True,
			"Europe": True,
			"Africa": True,
			"Oceania": True,
			"Northern America": True,
			"South America": True,
			"Western Asia": True
		}):
			
		if not test_environment:
			
			for region in regions_booleans:
				if regions_booleans[region] :
					GPIO.output(self.regions_leds[region], GPIO.HIGH) 
				else:
					GPIO.output(self.regions_leds[region], GPIO.LOW) 
				
				time.sleep(0.5)
			
			self.read_state()
