---
layout: default
title: 1-Setting Up a Raspberry Pi
nav_order: 2
parent: Workshop Activities
---

<img src="images/logo.png" alt="logo" style="float:right;width:180px;">

# Getting Setup

If you have any questions or get stuck as you work through this in-class exercise, please ask the instructor for assistance. Enjoy!

<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Formatting the SD card and Installing Raspbian**

1.  Open this document in your browser and so that you can click on the hyperlinks in the document:  http://bit.ly/2MCdL7r
2.  Download a copy of **Raspbian Buster with Desktop** from the [Raspberry Pi website](https://www.raspberrypi.org/downloads/raspbian/){:target="_blank"}  **Note:** if the download looks like it will take more than 5 minutes, ask your instructor for a thumb drive copy.
3.  Install the [Etcher disk imager](https://www.balena.io/etcher/){:target="_blank"} for Windows, Mac, and Linux on your computer
4.  Using Etcher burn the disk image onto the SD card (If your computer does not have an SD card reader, you can borrow one from the Music and Media desk in the library):
    -   Put the SD card into the USB adapter/micro-adapter then into your computer.
    -   Unzip the Raspbian file downloaded in step 1, and open Etcher.
    -   Follow the directions in Etcher to copy the file to the SD card.
5.  Raspbian is now installed onto the SD card!
    -   If you are on windows, eject the drive before removing the SD card.
    -   If you are on a mac the drive will be ejected for you. Go ahead and remove the SD card.
    -   Insert the card into the SD port of the Raspberry Pi, connect the peripherals, and power it up.

    <br>
    **Initial Setup of Raspbian**
    
6.  With all peripherals installed, allow the Raspberry Pi to boot into the desktop.
    -   The first thing you’ll be prompted to do will be to set up a new password, for the purposes of this lab set the password to be **raspberry**, or skip this step.
    -   When prompted, reboot your raspberry pi.
    -   Set the date and time on your raspberry pi:
        
        <img src="images/act-1/command-line-logo.png" alt="console icon" style="float:right;width:60;">
        
        -   Open the terminal by clicking on the icon on the top bar (see icon on right).
        -   In the terminal enter this command & press enter: **sudo date -s “mm/dd/yyyy hh:mm”**
            -   Example: **sudo date -s “01/28/2020 14:24”**
        -   Once this is done, enter this command & press enter: **sudo apt-get update**
            -   Outside of workshop, you would want to upgrade as well, but that would take a long time so we will not!
    
    <img src="images/act-1/globe-logo.png" alt="globe icon" style="float:right;width:60;">
    
    -   Navigate around, you’ll see a taskbar at the top of the desktop with the Chromium web browser icon (see right). Try launching it!
        -   After launching the web browser, see if you can connect to **google.ca**
        -   If you can, then your network settings are setup.
        -   Open this document in your browser on your Raspberry Pi so that you can click on the hyperlinks and copy and paste code from [this document](http://bit.ly/2MCdL7r){:target="_blank}

    <br>
    **Installing New Software on Raspbian**
    
7.  In a new terminal shell, we will install Python.
8.  Enter the command **sudo apt-get install gimp**
    
    <br>
    **Basic Python Programming, Hello World and Nano**
    
9.  With Python installed, open the terminal and enter: **python3**
    -   A new prompt should show up “**>>>**”. This is the Python shell.
0.  In here simple Python commands can be executed. Try entering **x = 5**, then **y = 8**. These variables, x and y, are now set as the values 5 and 8.
    -   Type in **x+y** and press enter
    -   Try some other basic arithmetic commands with these variables!
    -   When you’re done type: **exit()** and press enter.
1.  In case we want to save a program, we need to be able to create new files. To do so, we will use nano.
    -   Enter this command **sudo nano hello_world.py**
    -   In the nano window, type in **message = ‘Hello, world!’** then on a new line **print(message)**.
    -   Now, to save the file, enter the keystroke **ctrl+x**, then press **Y**, then **Enter**. You should now be back in the terminal.
    -   From here, type in **python3 hello_world.py**

    <br>
    **Extended Configuration**
    
2.  In the case that you need to, or want to, edit any of the core settings of the Raspberry Pi, open a terminal and execute this command: **sudo raspi-config**
3.  There are multiple configuration options here, to learn more checkout [this website](https://elinux.org/RPi_raspi-config){:target="_blank"}
4.  For an example of a useful feature, we will enable auto-login on the Raspberry Pi.
    -   After executing **raspi-config** navigate to **Boot Options** and press **Enter**
    -   Navigate to **Desktop/CLI** then to **Desktop Autologin** and **Enter**.
    -   You’ve now enabled autologin to the desktop.
    -   Navigate to the main menu, and hit **Tab** then **Exit** and reboot the Pi. It should now autoboot

    <br>
    **Projects:**
    
5.  Pick some projects!
    -   [Kiosk Computer](http://bit.ly/2ryOD9G){:target="_blank"}
    -   [Temp Log](http://bit.ly/38NjrnG){:target="_blank"}
    -   [Headless RbPi](http://bit.ly/3afHkoH){:target="_blank"}
6.  At Home projects
    -   [Lakka Retro Gaming Computer](http://bit.ly/33CDwL7){:target="_blank"}
    -   [C64 Disk Hack](http://bit.ly/2O7ajSP){:target="_blank"}

    <br>
    **Important Things:**
    
7.  How to shutdown the Raspberry Pi
    -   In the terminal, enter this command **sudo shutdown -h now**
    -   After installing large applications, update and upgrade your raspberry pi **(ONLY UPGRADE WHEN YOU HAVE A LOT OF TIME)**

[NEXT STEP: Retro Pi](act-2.html){: .btn .btn-blue }
