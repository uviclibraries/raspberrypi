---
layout: default
title: 3-Kiosk Computer
nav_order: 4
parent: Workshop Activities
---

<img src="images/act-3/logo-3.png" alt="kiosk" style="float:right;width:240px;">

# Kiosk Computer

If you have any questions or get stuck as you work through this in-class exercise, please ask the instructor for assistance. Enjoy!

## Installing Necessary Software

1.  In order to set up the Raspberry Pi as a Kiosk Computer, you will need to significantly alter the Pi’s software. The first handout has instructions on how to do so: [http://bit.ly/2MCdL7r](http://bit.ly/2MCdL7r){:target="_blank"}
2.  Firstly, prepare the pi by entering these commands:
    ```
    sudo apt-get clean
    sudo apt-get autoremove -y
    ```
3.  Now the latest versions must be installed, to do so, enter the command `sudo apt-get update`
4.  This may take a while, so as it is updating, let’s set up the slides we will display.
    -   You can display any website you like, or you can use a google slideshow.
    -   You can either create one now or use this one here:  [http://bit.ly/dsc-signage2](http://bit.ly/dsc-signage2){:target="_blank"}
5.  Once the Pi is done updating, install xdotool and sed using this command:
    ```
    sudo apt-get install xdotool unclutter sed
    sudo apt-get install x11-xserver-utils
    ```
6.  Navigate to the autostart directory, to do this, enter the command
    ```
    cd /etc/xdg/lxsession/LXDE-pi/
    ```
7.  Now, enter the command `sudo nano autostart`
8.  In this nano editor, copy in these lines:
    ```
    @chromium-browser --kiosk --incognito [your url]
    @xset s noblank
    @xset s off
    @xset -dpms
    @unclutter -idle 0.1 -root
    ```
9.  Now save and exit from nano by pressing "ctrl" and "X" then "Y".
10.  Enter in this command to the command line: `sudo nano /etc/lightdm/lightdm.conf`
11.  Add the following line to the end of the file, then save and exit: `Xserver-command = X -s 0 -dpms`
12.  Reboot the Pi: `sudo reboot`
13.  To exit kiosk mode, do the keystroke **ctrl+w**
14.  It is best practice to run kiosk mode on a Raspberry Pi with no log in prompt and no valuable data stored anywhere on the SD card. This way it can boot into the kiosk 
     screen without interruption.

[NEXT STEP: CPU Temperature Monitor](act-4.html){: .btn .btn-blue }
