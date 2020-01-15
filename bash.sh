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

# To install python requirements (file at the root of this git project):

sudo apt-get update
sudo apt-get upgrade

curl -sSL https://get.docker.com | sh
sudo usermod -aG docker pi
sudo docker run hello-world
sudo apt-get install libffi-dev libssl-dev
sudo apt-get install -y python3 python3-pip
# sudo apt-get remove python-configparser
# sudo pip3 install docker-compose
sudo apt install docker-compose

sudo docker network create iot-labs

sudo docker-compose -f $PWD/raspberry/influxdbgrafana/docker-compose.yml up -d

sudo docker ps -a



pip3 install -r requirements.txt

