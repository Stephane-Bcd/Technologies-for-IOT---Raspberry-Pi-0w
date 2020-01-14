Technologies for IOT - Raspberry Pi 0w


# Steps to make it work

Install needed packages using command:
sh bash.sh

# Tips for developers

Put all your linux packages (which need sudo apt install) inside of bash.sh
Put all your python libraries (which need pip install) inside requirements.txt


# Data retrieved from
Last 24 hours: https://www.gdacs.org/xml/rss_24h.xml

Last 48 hours magnitude > 4.5: https://www.gdacs.org/xml/rss_eq_48h_low.xml


#Topology of the LED/COUNTRIES

1- ROUGE = AMERIQUE DU NORD (pin-->GPIO 7)
2- BLANC = AMERIQUE DU SUD (pin-->GPIO 0)
3- VERT = EUROPE (pin-->GPIO 2)
4- JAUNE = AFRIQUE (pin-->GPIO 3)
5- ORANGE = ASIE DE L'OUEST (pin-->GPIO 4)
6- BLEU = ASIE DE L'EST (pin-->GPIO 5)
7- GRIS/NOIR = OCEANIE (pin-->GPIO 6)

(blanc/blanc : GND)
