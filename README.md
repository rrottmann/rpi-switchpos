# rpi-switchpos

A simple script that detects the position of a two-way switch.

## HEADER

We attach a two-way switch to the pins 6, 8 and 10 of the outmost row.
When we set pin 10 to high, we can detect either low or high on pin 8.

![Raspberry Pi Zero W GPIO Header Pinout](pi0w-pinout.jpg)

## Usage

```bash
$ sudo apt install -y rpi.gpio
$ sudo ./switchpos.py
unknown|pos0|pos1

```