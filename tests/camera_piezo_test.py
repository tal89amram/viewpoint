#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
from classes.piezo_player import PiezoPlayer
import globals as g
g.init()

GPIO.setwarnings(False)         # Turn off GPIO warnings
GPIO.setmode(GPIO.BCM)          # Broadcom pin numbers
piezo = PiezoPlayer(g.PIEZO)    # piezo buzzer

piezo.play_power_on_jingle()
time.sleep(1)
piezo.play_start_recording_jingle()
time.sleep(1)
piezo.play_paused_jingle()
time.sleep(1)
piezo.play_power_off_jingle()
time.sleep(1)
piezo.play_low_battery_storage_jingle()
