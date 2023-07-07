---
layout: default
title: 5-Electronics With The Raspberry Pi
nav_order: 6
parent: Workshop Activities
---

<img src="images/act-5/pi3-gpio.svg" alt="pi3 gpio" style="float:right;width:480px;">

# Electronics With The Raspberry Pi

If you have any questions or get stuck as you work through this in-class exercise, please ask the instructor for assistance. Enjoy!

## Blink
1.  We begin this activity with a classic example of GPIO (general purpose input or output) control. Connect an LED in series with a 220&Omega; resistor between GPIO pin 25 and ground.
2.  Create a new Python file: `sudo nano blink.py`
3.  Enter the following:
    ```
    import RPi.GPIO as gpio
    from time import sleep

    pin = 25
    gpio.setmode(gpio.BCM)
    gpio.setup(pin, gpio.OUT)

    while True:
        gpio.output(pin, gpio.HIGH)
        sleep(1)
        gpio.output(pin, gpio.LOW)
        sleep(1)
    ```
4.  Save and exit by pressing "ctrl" and "X" then "Y".
5.  Run the Python script and watch the LED blink on and off: `python3 blink.py`
6.  Press "ctrl" and "C" to exit the program.
7.  Note that exiting while the LED is on will cause it to stay on.

## Push Button
8.  Connect a momentary push button in series with a 10k&Omega; resistor between GPIO pin 25 and 3.3 volt power.
9.  
