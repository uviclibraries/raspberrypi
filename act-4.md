---
layout: default
title: 4-CPU Temperature Monitor
nav_order: 5
parent: Workshop Activities
---

<img src="images/act-4/logo-4.png" alt="logo" style="float:right;width:180px;">

# Raspberry Pi CPU Temperature Log

If you have any questions or get stuck as you work through this in-class exercise, please ask the instructor for assistance. Enjoy!

## Installing The Necessary Software 
1.  Open up a terminal shell, this can be done by clicking on its icon (see right) <img src="images/act-1/terminal-icon.png" alt="console icon" style="float:right;width:60px;">
    -   Alternatively, a new shell can be opened by pressing `crtl+alt+t`
2.  Next, ensure that matplotlib is installed by entering the command `sudo apt-get install python3-matplotlib`
3.  If it installs or confirms that matplotlib is installed, proceed to the next step.

## Creating The Python Script <img src="images/logo.png" alt="logo" style="float:right;width:60px;">
4.  Enter `python3` to open the Python interpreter.
6.  Enter these lines of code in order:
    ```
    from gpiozero import CPUTemperature
    cpu = CPUTemperature()
    print(cpu.temperature)
    ```
    This simply gets the temperature of the CPU and prints it.
7.  Press "ctrl" and "D" on your keyboard to exit the Python interpreter.
8.  Create a new Python file: `sudo nano cpu_temp.py`
9.  Now let’s make the script more robust by having a log of the temperatures. To do this, enter the following lines:
    ```
    from gpiozero import CPUTemperature
    from time import sleep, strftime, time
    from gpiozero import CPUTemperature
    cpu = CPUTemperature()
    
    with open(“cpu_temp.csv”, “a”) as log:
        while True:
            temp = cpu.temperature
            log.write(‘{0},{1}\n’.format(strftime(‘%Y-%m-%d %H:%M:%S’), str(temp)))
    ```

10.  Running this code will keep a log in the form of a CSV file. This file can be found in /home/pi and will be called cpu_temp.csv.
11.  Try running the code and finding the file.
12.  Now that a log is kept, visualization in the form of a realtime graph can be scripted.
13.  Enter this to draw a graph of the temperature:
     ```
     from gpiozero import CPUTemperature
     from time import sleep, strftime, time
     import matplotlib.pyplot as plt

     cpu = CPUTemperature()
     x = []
     y = []

     def write_temp(temp):
         with open('cpu_temp.csv', 'a') as log:
             log.write('{0},{1}\n'.format(strftime('%Y-%m-%d %H:%M:%S'), str(temp)))

     def graph(temp):
         y.append(temp)
         x.append(time())
         plt.clf()
         plt.scatter(x, y)
         plt.plot(x, y)
         plt.draw()

     while True:
         temp = cpu.temperature
         write_temp(temp)
         graph(temp)
         plt.pause(1)
     ```

## Run on Startup
14.  This Python script can be made to run automatically on boot.
15.  Open a new terminal window and enter in `crontab -e` to open crontab.
    -   If prompted, choose nano from the options given.
16.  Scroll to the bottom of the opened file and enter in this line in a new line: `@reboot python3 /home/pi/temp.py`
17.  Now, reboot the Raspberry Pi by entering the command: `sudo reboot`
18.  Once the Raspberry Pi is rebooted and has run for a bit, enter the command: `cat cpu_temp.csv`
19.  This will display a log of the recent CPU temperature.

[NEXT STEP: Electronics and The Raspberry Pi](act-5.html){: .btn .btn-blue }
