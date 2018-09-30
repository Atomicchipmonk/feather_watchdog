This is the first attempt at building a monitoring system for the Jetson TX2. It uses influxDB and the TICK stack as the backend with a Adafruit Feather 32a4 board connected to a ina219 chip for current sensing.


Hardware:
This is intended to monitor a Jetson TX2, however it should be able to be used on any linux platform with USB.

Current Sensor Setup:
Feather board (chose 32u4 BasicProto)
INA219 FeatherWing

Download the arduino INA219 library into your arduino library directory
https://github.com/adafruit/Adafruit_INA219

Compile and load the sketch to the feather board. It should now be outputting current and voltage over serial.

TX2 setup:

It requires the following packages:
docker
docker-compose
lm-sensors

In repo top level directory run:
docker build -t feather_watchdog .
docker-compose up -d

This should build the feather_watchdog container, pull down the TICK stack and start the TICK service. You can reach it here:
http://localhost:8888

Start playing around!
