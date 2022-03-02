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
    A
    if current_time == time(15) or current_time == time(10,30 ):
            print("Job wird gestartet")  
            # do stuff
            sleep(60)
    else:
            print("error")
            sleep(60)
            goto :A
KeyboardInterrupt
