---
layout: default
title: 4-CPU Temperature Monitor
nav_order: 5
parent: Workshop Activities
---

<img src="images/act-4/logo-4.png" alt="logo" style="float:right;width:180px;">

# Raspberry Pi CPU Temperature Log

If you have any questions or get stuck as you work through this in-class exercise, please ask the instructor for assistance. Enjoy!

<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Installing Needed Software**
    
    <img src="images/act-4/command-line-logo.png" alt="console logo" style="float:right;width:180px;">
    
1.  Open up a terminal shell, this can be done by clicking on this icon
    -   Alternatively, a new shell can be opened by pressing `crtl+alt+t`
2.  Next, ensure that matplotlib is installed by entering the command `sudo apt-get install python3-matplotlib`
3.  If it installs or confirms that matplotlib is installed, proceed to the next step.

    <br>
    **Creating the Python Script**
    
4.  Open a new blank Python file by **Menu > Programming > Mu**
    -   The menu is the RaspberryPi logo in the top left.
5.  After launching Mu, select **Python 3** and click **OK**
6.  In Mu, under the first commend enter in these lines of code:

    ```
    from gpiozero import CPUTemperature
    cpu = CPUTemperature()
    ```

7.  Save the program as **temp** then click **Run**
    -   A run time menu will appear with a **>>>** as a prompt.
    -   Type in `cpu.temperature` to this prompt to get a temperature readout of the CPU in Celcius
8.  Now, let’s make the script more robust by having a log of the temperatures. To do this, copy in the following lines:

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

9.  Running this code will keep a log in the form of a CSV in the designated folder. This folder can be found in /home/pi and will be called cpu_temp.csv.
0.  Try running the code and finding the file.
1.  Now that a log is kept, visualization in the form of a realtime graph can be scripted.
2.  Copy over the following code to the script, save and run.

    ```
    from gpiozero import CPUTemperature
    from time import sleep, strftime, time
    import matplotlib.pyplot as plt

    cpu = CPUTemperature()

    def write_temp(temp):
    with open(‘cpu_temp.csv’, ‘a’) as log:
        log.write(‘{0},{1}\n’.format(strftime(‘%Y-%m-%d %H:%M:%S’), str(temp)))
    def graph(temp):
    y.append(temp)
    x.append(time())
    plt.clf()
    plt.scatter(x,y)
    plt.plot(x,y)
    plt.draw()

    while True:
        temp = cpu.temperature
        write_temp(temp)
        graph(temp)
        plt.pause(1)
    ```

3.  Save and run this script to get a graph of the current cpu temperature.

    <br>
    **Automating the Script**

4.  This Python script can be made to run automatically on boot.
5.  Open a new terminal and enter in `crontab -e` to open crontab
    -   If prompted, choose nano from the options given
6.  Scroll to the bottom of the opened file and enter in this line in a new line:

    ```
    @reboot python3 /home/pi/temp.py
    ```

7.  Now, reboot the Raspberry Pi by entering the command `sudo reboot`
8.  Once the pi has reboot and run for a bit, enter the command `cat cpu_temp.csv`
9.  This will display a log of the recent CPU temperature.

[NEXT STEP: Earn a Workshop Badge](informal-credentials.html){: .btn .btn-blue }
