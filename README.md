# Experiment with Node-RED


 [Sense Hat](https://www.raspberrypi.org/documentation/hardware/sense-hat/) sensors, joystick and dot matrix using the [node-red-node-pi-sense-hat](https://flows.nodered.org/node/node-red-node-pi-sense-hat) node. Follow the instructions below, install all prerequisites and import the given flows into your Node-RED installation using the import dialogue. The Node-RED panel - [how to install Node-RED on a Raspberry Pi](https://nodered.org/docs/getting-started/raspberrypi) - is available under `http://<IP of your Pi>:1880` and the Node-RED Dashboard can be reached with  `http://<IP of your Pi>:1880/ui`:



## Pre-requisites

### Installing Python 3.7.0 on Raspbian

Install the required build-tools:

```bash
sudo apt-get install build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev -y
```

Download and install Python 3.7.0 When downloading the source code:

```bash
wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tar.xz
tar xf Python-3.7.0.tar.xz
cd Python-3.7.0
./configure
make -j 4
sudo make altinstall
sudo apt-get install python3-pip
```

### Installing the Sense HAT python drivers

```bash
sudo apt-get update
sudo apt-get install sense-hat
sudo pip3 install pillow
```

Then install the [node-red-node-pi-sense-hat](https://flows.nodered.org/node/node-red-node-pi-sense-hat) node in [Node-RED](https://nodered.org/) and [node-red-dashboard](https://flows.nodered.org/node/node-red-dashboard) from the Palette menu:

## FLOW 1 : Read procesador data 

### Diagram 
![FLOW1](https://github.com/crissmath/NODE-RED-PROJECT/blob/master/Pictures/Flow1.png)
### Flow 
![FLOW1](https://github.com/crissmath/NODE-RED-PROJECT/blob/master/Pictures/Imagen6.png)

