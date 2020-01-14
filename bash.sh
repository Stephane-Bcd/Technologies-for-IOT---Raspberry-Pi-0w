# This is a file of commands executed on Raspberry Pi 3B

# default logins for raspberry:
# Username 	Password
# pi 	    raspberry

# changed to:
# Username 	Password
# pi 	    not changed
# root 	    not changed

# Command to change password: psswd
# same for root with 'sudo passwd root' command

# ATTENTION RASPBERRY IS BY DEFAULT IN QWERTY changed to AZERTY using following :
# RASPBERRY CONFIGURATION INTERFACE:
# sudo raspi-config
# changed localisation option keyboard layout

# to clone repository
# git clone "https://github.com/Stephane-Bcd/Technologies-for-IOT---Raspberry-Pi-0w" "./Tech for IOT"
 
 # data retrieved from
 # https://www.gdacs.org/xml/rss_24h.xml

# To install python requirements (file at the root of this git project):
sudo apt install python3
sudo apt install python3-pip
pip3 install -r requirements.txt

