---
layout: default
title: 5-Electronics With The Raspberry Pi
nav_order: 6
parent: Workshop Activities
---

<img src="images/act-2/logo-2.png" alt="retro pi" style="float:right;width:180px;">

# Electronics With The Raspberry Pi

If you have any questions or get stuck as you work through this in-class exercise, please ask the instructor for assistance. Enjoy!

## Blink
1.  We begin this activity with a classic example of GPIO (general purpose input or output) control. Create a new Python file: `sudo nano blink.py`
2.  Enter the following:
    ```
    import RPi.GPIO as gpio
    from time import sleep

    gpio.setmode(gpio.BCM)
    gpio.setup(14, gpio.OUT)

    while True:
        gpio.output(14, gpio.HIGH)
        sleep(1)
        gpio.output(14, gpio.LOW)
        sleep(1)
    ```
3. Save and exit by pressing "ctrl" and "X" then "Y".
4. Connect an LED in series with a resistor between GPIO pin 14 and ground.
5. Run the Python script and watch the LED blink on and off every one second: `python3 blink.py`
6. Press "ctrl" and "C" to exit the program.

## ???
