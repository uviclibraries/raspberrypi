---
layout: default
title: 2-Retro Pi
nav_order: 3
parent: Workshop Activities
---

<img src="images/act-2/logo-2.png" alt="retro pi" style="float:right;width:180px;">

# Retro Gaming With RetroPi
If you have any questions or get stuck as you work through this in-class exercise, please ask the instructor for assistance. Enjoy!

## Installing The Necessary Software
1.  Install the dependencies of the RetroPie setup script: `sudo apt install git lsb-release`
2.  Download the RetroPie setup script from GitHub: `git clone --depth=1 https://github.com/RetroPie/RetroPie-Setup.git`
3.  Run the installation script:
    ```
    cd RetroPie-Setup
    chmod +x retropie_setup.sh
    sudo ./retropie_setup.sh
    ```
    In the interest of saving time, we will install emulators individually instead of proceeding with the full RetroPie installation.
5.  Navigate to `Manage packages -> core`  then `Install all core packages` (~8 Minutes)
6.  Navigate to `Manage packages -> main -> lr-mame2003` then `Install from pre-compiled binary` (~2 Minutes)

## Running RetroPie
7.  Using the Raspberry Pi desktop file explorer, navigate to `/home/pi/RetroPie/roms/arcade` and copy over a MAME compatible arcade game ROM.
8.  Run the command: `emulationstation`
9.  You will be prompted to configure the RetroPie controls.
10.  Using the controls that have been assigned, navigate to the arcade game and try running it.

# Start of Old Content

## Installing Necessary Software
1.  Install a copy of RetroPi at [this site](https://retropie.org.uk/download/){:target="_blank"} for the appropriate hardware.
2.  After getting the image, run etcher and load the image onto the microSD card.
3.  This may take a while, so as it loads, go to [this site](https://www.downloadroms.io/){:target="_blank"} to find some ROMs you’d like to play!
4.  Once finished, insert the microSD into the RaspberryPi and turn it on
5.  You will now configure the game controller, for this lab, we will use the keyboard.
6.  **TO SKIP OTHER STEPS** hold down any already bound key. Continue doing this for keys not listed.
7.  Ensure that the d-pad up, down, left, right keys are set (suggest WASD for these)
8.  Ensure that the A,B,X, and Y buttons are bound (numpad up, right, left, and down are recommended)
9.  The **A** button will be your primary selection method as opposed to a keyboard and mouse.
0.  Ensure start and select are bound (z and x recommended)
1.  At this point, you will skip a lot of buttons until the botbutton is reached at the bottom of the menu.
2.  Ensure that the **HOTBUTTON** is set (suggest **ENTER**)

## Downloading and Running New Game Software
3.  After downloading a couple of ROMs, we need to setup a USB stick to hold these ROMs.
4.  With a blank USB stick, format it to a FAT32 or NTFS format
5.  Create a file in the USB stick, and name it **retropie**
6.  Ensure that the Pi is turned off at this point before continuing
7.  Plug the USB into the pi, and wait for the pi to stop blinking (about a minute)
8.  Let the Pi completely boot to the retropie main menu.
9.  Reboot the Pi by hitting the F4 key and typing into the terminal `sudo reboot`
0.  Then shutdown the pi and unplug the usb
1.  Load the ROMs into the **retropie/roms** folder
2.  Now you can plug it back in and play.

## Accessories
3.  If you would like to do this at home, a USB game control will work well for most games.
4.  A keyboard and mouse are good things to have installed at all times. If something goes wrong you can quit to a terminal menu with the **ctrl+f1** key combo.

## Important Information
5.  Changing games: hold down the hotkey, select, and start to exit to the main menu.

[NEXT STEP: Kiosk Computer](act-3.html){: .btn .btn-blue }
