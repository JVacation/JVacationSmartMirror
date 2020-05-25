JVacation Smart Mirror featuring Facial Recognition and Security

Made to be ran on a Raspberry Pi but to do pandemic I suggest using:

Virtual Box: https://www.virtualbox.org/
Raspberry Pi Desktop: https://www.raspberrypi.org/downloads/raspberry-pi-desktop/

On instructions to install Raspberry Pi Desktop follow:
https://thepi.io/how-to-run-raspberry-pi-desktop-on-windows-or-macos/

Project video here: https://www.youtube.com/watch?v=BgjUwgD4-U4

##### Web Cam Support ######

Some webcams do not ship with drivers for raspbian. To use a usb webcam or built in webcam with virtual box use the virtual box extension pack. https://www.Virtualbox.Org/wiki/download_old_builds_6_0 make sure you get the same version of extension pack as your virtual box installation

To use the webcam via extension pack go to the virtual machine toolbar > devices > webcams > select webcam



###### Installing the Software ######

1) Extract the project to the Desktop.

2) Open a Terminal and type: CD Desktop/JVacationSmartMirror-master/

3) sudo apt-get install cmake

4) pip3 install -r requirements.txt // This step can take a while so go make a brew and come back.

5) Once completed type: cd webserver

6) sudo apt-get update

7) sudo apt install nodejs

8) sudo apt install npm

9) sudo npm install socket.io --save

10) CD back to the main directory (JVacatonSmartMirror-master) and to launch the mirror run:

11) python3 mirror.py

The smart mirror should now start up.

To disable the camera preview open mirror.py with a code editor and change:

enableCameraPreview = "enable"

to:

enableCameraPreview = "disable"


If it comes up with can't open camera by index it means a camera is not detected. Please follow the Virtualbox extension guide above.

Test: Use the camera on a picture of Joe Biden. He is the figure stored to ensure that the system is working.



###### Adding users ######

Navigate to localhost:3000 in a browser and follow the steps shown

If using a external device such as phone connect to the ip displayed on the mirror's main screen



##### Changing Security Settings #####

To change the timezone of when the mirror should save frames of unknown users open up cam.py with a code editor.
There are two lines called:
start = datetime.time(10, 15)
end = datetime.time(11)

Change these to the timezone wanted. For instance 9am-5:30pm will be:
start = datetime.time(9)
end = datetime.time(17, 30)

A web server interface will be developed for this later.
