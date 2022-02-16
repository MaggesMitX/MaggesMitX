#!/usr/bin/env python3
# coding: utf-8

import time
import struct
from pyModbusTCP.client import ModbusClient
from pyModbusTCP import utils

#import influxdb_client
#from influxdb_client.client.write_api import SYNCHRONOUS

#init modbus client
client = ModbusClient(host="10.168.16.123", port=502, unit_id=1, auto_open=True, auto_close=True)

#read all registers from one to 18
regs_to_read = 18 
regs = client.read_input_registers(0x0000, regs_to_read)


def bin_to_float(binary, start):
    return struct.unpack('>f', bytes.fromhex(f"{binary[start]:0>4x}" + f"{binary[start+1]:0>4x}"))[0]

if regs:
    for i in range(3):
        print("L%d:\t%3.3f V\t%3.3f A\t%3.3f W" % (i+1, bin_to_float(regs, 2*i), bin_to_float(regs, 2*i+6), bin_to_float(regs, 2*i+12)))
else:
    print("read error")

#Define Variables of Influx Client
#bucket = "<my-bucket>"
#org = "<my-org>"
#token = "<my-token>"
# Store the URL of your InfluxDB instance
#url="https://us-west-2-1.aws.cloud2.influxdata.com"

#Init the Client 
#client = influxdb_client.InfluxDBClient(
#   url=url,
#   token=token,
#   org=org
#)
# read 3 coils at @0 on localhost server
#print('coils=%s' % ModbusClient().read_coils(0, 3))


