#!/usr/bin/env python3
# coding: utf-8
#python library mit pip install qrcode

import qrcode

img = qrcode.make(
    'https://google.com/de/'
)
img.save(qrcode.png)
img.show
