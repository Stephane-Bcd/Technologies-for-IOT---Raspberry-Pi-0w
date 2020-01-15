#environnement : python3
#-- coding: utf-8 --

import RPi.GPIO as GPIO #Importe la bibliothèque pour contrôler les GPIOs

GPIO.setmode(GPIO.BOARD) #Définit le mode de numérotation (Board)
GPIO.setwarnings(False) #On désactive les messages d'alerte

NORTH_AMERICA_LED = 7 #Définit le numéro du port GPIO qui alimente la led

GPIO.setup(NORTH_AMERICA_LED, GPIO.OUT) #Active le contrôle du GPIO

state = GPIO.input(NORTH_AMERICA_LED) #Lit l'état actuel du GPIO, vrai si allumé, faux si éteint

if state : #Si GPIO allumé
    GPIO.output(NORTH_AMERICA_LED, GPIO.LOW) #On léteint
else : #Sinon
    GPIO.output(NORTH_AMERICA_LED, GPIO.HIGH) #On l'allume
