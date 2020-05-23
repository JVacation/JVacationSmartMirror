JVacation Smart Mirror featuring Facial Recognition and Security

Made to be ran on a Raspberry Pi but to do pandemic I suggest using:

Virtual Box: https://www.virtualbox.org/
Raspberry Pi Desktop: https://www.raspberrypi.org/downloads/raspberry-pi-desktop/

On instructions to install Raspberry Pi Desktop follow:
https://thepi.io/how-to-run-raspberry-pi-desktop-on-windows-or-macos/

SOME WEBCAMS DO NOT SHIP WITH DRIVERS FOR RASPBIAN. TO USE A USB WEBCAM OR BUILT IN WEBCAM WITH VIRTUAL BOX USE THE VIRTUAL BOX EXTENSION PACK
https://www.virtualbox.org/wiki/Download_Old_Builds_6_0 MAKE SURE YOU GET THE SAME VERSION OF EXTENSION PACK AS YOUR VIRTUAL BOX INSTALLATION

TO USE THE WEBCAM VIA EXTENSION PACK GO TO THE VIRTUAL MACHINE TOOLBAR>DEVICES>WEBCAMS>SELECT WEBCAM

Installing the Software:

Extract the project to the Desktop.

Open a Terminal and type: CD Desktop/JVacationSmartMirror-master/

sudo apt-get install cmake

pip3 install -r requirements.txt

This step can take a while so go make a brew and come back.

Once completed type: cd webserver

Run:

sudo apt-get update

sudo apt install nodejs

sudo apt install np

Followed by:

sudo npm install socket.io --save

Well done it should now be installed.

CD back to the main directory (JVacatonSmartMirror-master) and to launch the mirror run:
python3 mirror.py

If it comes up with can't open camera by index it means a camera is not detected. Please follow the Virtualbox extension guide above.