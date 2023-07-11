---
layout: default
title: 5-Electronics and The Raspberry Pi
nav_order: 6
parent: Workshop Activities
---

<img src="images/act-5/pi3-gpio.svg" alt="pi3 gpio" style="float:right;width:480px;">

# Electronics and The Raspberry Pi

If you have any questions or get stuck as you work through this in-class exercise, please ask the instructor for assistance. Enjoy!

## Blink
1.  We begin this activity with a classic example of GPIO (general purpose input or output) control. Connect an LED in series with a 220&Omega; resistor between GPIO pin 25 and ground. <br><img src="images/act-5/pi-blink-diagram.png" alt="blink" style="float:center;width:480px;">
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
    The pin numbering is set to the Broadcom CPU's definitions with `gpio.setmode(gpio.BCM)` and pin 25 is initialized as an output with `gpio.setup(pin, gpio.OUT)`<br>
    GPIO pins can be in one of two states:
    -   0V (ground): `gpio.LOW`
    -   3.3V: `gpio.HIGH`
4.  Save and exit by pressing "ctrl" and "X" then "Y".
5.  Run the program and watch the LED blink on and off: `python3 blink.py`
6.  Press "ctrl" and "C" to exit the program.
    -   Note that exiting while the LED is on will cause it to stay on.

## Push Button
7.  Connect a momentary push button in series with a 10k&Omega; resistor between GPIO pin 25 and 3.3V power. <br><img src="images/act-5/pi-button-diagram.png" alt="button" style="float:center;width:480px;">
8.  Create a Python file named `button.py` and enter the following:
    ```
    import RPi.GPIO as gpio

    pin = 25
    gpio.setmode(gpio.BCM)
    gpio.setup(pin, gpio.IN, pull_up_down=gpio.PUD_DOWN)

    while True:
        if gpio.input(pin) == gpio.HIGH:
            print("Button Pushed")
    ```
    The new parameter `pull_up_down=gpio.PUD_DOWN` will internally connect the pin to ground with a very high value resistor.
9.  Run the program and then press the button. The terminal should be filled with "Button Pushed" due to the while loop repeating many times per second.
10.  In some cases, a more useful approach to GPIO input is callbacks. These work by interrupting the program to call a function. In this example, `buttonPressedCallback` will interrupt a counting process:
     ```
     import RPi.GPIO as gpio
     from time import sleep

     def buttonPressedCallback(channel):
         print("Pressed")

     pin = 25
     gpio.setmode(gpio.BCM)
     gpio.setup(pin, gpio.IN, pull_up_down=gpio.PUD_DOWN)
     gpio.add_event_detect(pin, gpio.RISING, callback=buttonPressedCallback)
     i = 0
     
     while True:
         print(i)
         i = i + 1
         sleep(1)
     ```
     The parameter `gpio.RISING` specifies calling the function when the state changes from low to high. Alternatively, `gpio.FALLING` could have been used for high to low or `gpio.BOTH` for either case.

## Pulse Width Modulation
11.  Connect an LED to pin 25 like in the blink example.
12.  Create a Python file named `fade.py` and enter the following:
     ```
     import RPi.GPIO as gpio
     from time import sleep

     pin = 25
     gpio.setmode(gpio.BCM)
     gpio.setup(pin, gpio.OUT)

     pwm = gpio.PWM(pin, 100)
     pwm.start(0)

     for dc in range(0, 100, 1):
         pwm.ChangeDutyCycle(dc)
         sleep(0.05)

     for dc in range(100, 0, -1):
         pwm.ChangeDutyCycle(dc)
         sleep(0.05)

     pwm.ChangeDutyCycle(0)
     ```
     Pin 25 is assigned pulse width modulation and the duty cycle (duration  of very fast pulses) is increased then decreased incrementally.
13.  Upon running this program, the LED will appear to get brighter then dimmer.

## Analog Input
14.  
