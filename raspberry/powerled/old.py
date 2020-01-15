#environnement : python3
#-- coding: utf-8 --

import RPi.GPIO as GPIO #Importe la bibliothèque pour contrôler les GPIOs
import time

GPIO.setmode(GPIO.BOARD) #Définit le mode de numérotation (Board)
GPIO.setwarnings(False) #On désactive les messages d'alerte

#Définit le numéro du port GPIO qui alimente la led

NORTH_AMERICA_LED = 7 
SOUTH_AMERICA_LED = 0
EUROPE_LED = 2
AFRICA_LED = 3
WEST_ASIA_LED = 4
EAST_ASIA_LED = 5
OCEANIA_LED = 6

GPIO.setup(NORTH_AMERICA_LED, GPIO.OUT) #Active le contrôle du GPIO
GPIO.setup(SOUTH_AMERICA_LED, GPIO.OUT)
GPIO.setup(EUROPE_LED, GPIO.OUT)
GPIO.setup(AFRICA_LED, GPIO.OUT)
GPIO.setup(WEST_ASIA_LED, GPIO.OUT)
GPIO.setup(EAST_ASIA_LED, GPIO.OUT)
GPIO.setup(OCEANIA_LED, GPIO.OUT)

#Lit l'état actuel du GPIO, vrai si allumé, faux si éteint

NORTH_AMERICA_LED_state = GPIO.input(NORTH_AMERICA_LED)
SOUTH_AMERICA_LED_state = GPIO.input(SOUTH_AMERICA_LED)
EUROPE_LED_state = GPIO.input(EUROPE_LED)
AFRICA_LED_state = GPIO.input(AFRICA_LED)
WEST_ASIA_LED_state = GPIO.input(WEST_ASIA_LED)
EAST_ASIA_LED_state = GPIO.input(EAST_ASIA_LED)
OCEANIA_LED_state = GPIO.input(OCEANIA_LED)

if NORTH_AMERICA_LED_state and SOUTH_AMERICA_LED_state and EUROPE_LED_state and AFRICA_LED_state and WEST_ASIA_LED_state and EAST_ASIA_LED_state and OCEANIA_LED_state :
    GPIO.output(NORTH_AMERICA_LED, GPIO.LOW) 
    time.sleep(0.5)
    GPIO.output(SOUTH_AMERICA_LED, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(EUROPE_LED,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(AFRICA_LED,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(WEST_ASIA_LED,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(EAST_ASIA_LED,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(OCEANIA_LED,GPIO.LOW)
else :
       GPIO.output(NORTH_AMERICA_LED, GPIO.HIGH) 
    time.sleep(0.5)
    GPIO.output(SOUTH_AMERICA_LED, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(EUROPE_LED,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(AFRICA_LED,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(WEST_ASIA_LED,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(EAST_ASIA_LED,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(OCEANIA_LED,GPIO.HIGH)
