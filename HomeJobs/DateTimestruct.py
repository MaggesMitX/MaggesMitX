#!/usr/bin/env python3
# coding: utf-8

from datetime import datetime, time

# get rid of exact seconds and microseconds
current_time = datetime.now().time().replace(second=0, microsecond=0)

if current_time == time(15) or current_time == time(18, 30):
    print("Test")
    # do stuff