#!/usr/bin/env python3

from pynput.keyboard import Key, Controller
from time import sleep,strftime
from datetime import datetime
import random

keyboard = Controller()
sleep(3) # Wait a few seconds to give focus to another window if desired
keypresses = 1

while True:
    now = datetime.now().strftime('%H:%M:%S')
    print('Fakeuser presses a key at %s (%s keypresses so far) - ' % (now, str(keypresses)), end='')
    waitTime = random.randint(420,500)
    keyboard.press(Key.ctrl)
    keyboard.release(Key.ctrl)
    print('Waiting %s seconds...' % (str(waitTime)))
    sleep(waitTime)
    keypresses += 1

