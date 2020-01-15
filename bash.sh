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
sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
    
curl -fsSL "https://download.docker.com/linux/ubuntu/gpg" | sudo apt-key add -

sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
   
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose

sudo docker run hello-world

sudo docker network create iot-labs

sudo docker-compose -f $PWD/raspberry/influxdbgrafana/docker-compose.yml up -d

sudo docker ps -a



sudo apt install python3
sudo apt install python3-pip
pip3 install -r requirements.txt

