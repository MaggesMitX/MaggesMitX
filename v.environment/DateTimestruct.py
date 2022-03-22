#!/usr/bin/env python3
# coding: utf-8

from datetime import datetime, time
from dis import findlinestarts
from re import A
from time import sleep
from turtle import goto

# get rid of exact seconds and microseconds
current_time = datetime.now().time().replace(second=0, microsecond=0)

while True:
    
    if current_time == time(8,35 ) or current_time == time(8,37 ):
            print("Job wird gestartet")  
            # do stuff
            sleep(5)
    elif current_time != time(15,00 ):
            print("error")
            sleep(5)
            break
    KeyboardInterrupt
