#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2020 Reiner Rottmann. All rights reserved.
# Released under BSD License. See LICENSE.txt

import importlib.util

try:
    importlib.util.find_spec('RPi.GPIO')
    import RPi.GPIO as GPIO
except ImportError:
    """
    import FakeRPi.GPIO as GPIO
    OR
    import FakeRPi.RPiO as RPiO
    """
    import FakeRPi.GPIO as GPIO

GPIO.setwarnings(False)

'''
       sw
> SD ##xxx###############
>   0###################
'''
GPIO.setmode(GPIO.BOARD)           # choose BCM or BOAR

GPIO.setup(10, GPIO.OUT)           # set pin 10 as an output
GPIO.output(10, GPIO.HIGH)         # set pin 10 as high

GPIO.setup(8, GPIO.IN)             # set pin 8 as input

# as pin 6 is GND, we can now detect low or high on pin 8 - thus our switch position
switchpos = 'unknown'
if GPIO.input(8) == GPIO.HIGH:
    switchpos = 'pos1'
if GPIO.input(8) == GPIO.LOW:
    switchpos = 'pos0'

print(f'{switchpos}')