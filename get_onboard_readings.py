import time
import requests

def read_input(current_name, decimator, unit):
  current_fd = open('/sys/devices/3160000.i2c/i2c-0/0-0041/iio_device/'+current_name)
  current = float(current_fd.read()) / decimator
  line='power_data ' + current_name.replace('input', unit) + '=' + str(current)
  current_fd.close()
  return line



current_input_list=[
"in_current0_input",
"in_current2_input",
"in_current1_input"]

voltage_input_list=[
"in_voltage0_input",
"in_voltage1_input",
"in_voltage2_input"]

power_input_list=[
"in_power0_input",
"in_power1_input",
"in_power2_input"]


while True:
  for input in current_input_list:
    line = read_input(input, 10, 'mAmps')
    print line
    try:
      resp = requests.post('http://192.168.1.110:8086/write?db=tx2i_1', data=line)
      print resp
    except:
     print "Unable to connect"
  for input in voltage_input_list:
    line = read_input(input, 1000, 'Volts')
    print line
    try:
      resp = requests.post('http://192.168.1.110:8086/write?db=tx2i_1', data=line)
      print resp
    except:
     print "Unable to connect"
  for input in power_input_list:
    line = read_input(input, 10000, 'Watts')
    print line
    try:
      resp = requests.post('http://192.168.1.110:8086/write?db=tx2i_1', data=line)
      print resp
    except:
     print "Unable to connect"


  time.sleep(1)
line.close()

