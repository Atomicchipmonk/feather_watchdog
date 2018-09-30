
import serial
import requests

ser = serial.Serial('/dev/ttyACM0', 115200, timeout=2)

while True:
  line=ser.readline().rstrip()
  print line
  try:
    resp = requests.post('http://influxdb:8086/write?db=arduino', data=line)
    print resp
  except:
   print "Unable to connect"
