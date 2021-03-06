# MyoCoach
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->




<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a >
    <img src="image/logo.png" alt="Logo" width="600" height="400">
  </a>

 



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <ul>
            <li><a href="#Make-the-box">Make the box</a></li>
            <li><a href="#Boards-Preparation">Boards Preparation</a></li>
            <li><a href="#Electrodes placement protocol">Electrodes placement protocol</a></li>
            <li><a href="#Programmation">Programmation</a></li>
        </ul>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li> 
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

In this repo you will find a second version of this [project](https://github.com/orthopus/01-myocoach). We have tried to make  this project more portable, accessible on different platforms (pc, smartpahones, tablets ...)
The MyoCoach is a device intended for people with upper limb amputees wishing to wear a myoelectric prosthesis made up of 2 EMG electrodes.

It allows you to exercise the contraction of the muscles of the forearm thanks to a video game inspired by Flappy Bird, and to train in the control of the future prosthesis.

The MyoCoach can also be addressed to health professionals and more particularly to orthopedic and occupational therapists, because it allows to correctly place the myoelectric sensors and to adjust them for an optimal use of myoelectric prostheses.

The MyoCoach allows you to:

<ul>
        <li> Measure muscle potential using myoelectric sensors</li>
        <li> Define the optimal position of the sensors</li>
        <li> Adjust the sensors using the potentiometers </li>
        <li> Practice muscle contraction and coordination</li>
  <li> Very ergonomic and flexible display of emg signals </li>
  <li> Serious game  to familiarize  without annoying with EMGs </li>
        
 </ul>


### Built With
To concrate our idea, we built this app with the following language : 
* [HTML](https://html.com/)
* [CSS](https://css-tricks.com/)
* [Javascript](https://www.javascript.com/)
* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)




<!-- GETTING STARTED -->
## Getting Started

The idea is to use the screen of a smartphone, a tablet or a pc to display the application. The system is intended to be very flexible, easy to use inexpensive and portable. A small portable box for example will contain all the device.


### Prerequisites
You must at least own these 4 things
* [Raspberry pi ](https://www.raspberrypi.org/)
* [Arduino](https://www.arduino.cc/)
* [2 EMG sensor]
* [USB cable]

### Principle diagram

This principle diagram summarizes the interactions between the different components of the project
<a >
    <img src="image/myocoach1.png" alt="Logo" width="1000" height="600">
  </a>
  
  The role of the arduino board is to receive the analog signals and convert them to digital and finally to send them via the serial port to the raspberry pi board. The raspberry pi board is the main element of our system.It receives EMG data from the arduino board at any time. It creates the web server and a hospot directly when it starts up. The user can connect to this network and thus access the application to view the ELG data or play the serious game.

### Installation

You can design the MyoCoach for less than **70€**. More details in the [COSTS](cost.md) file.

Follow this steps to make your own **MyoCoach**

# Make the box

In this manual you will find all the resources to design the various components of the MyoCoach. You will see that we don't take into account the raspberry pi emplacement, you can make externe by using his base box or adding it in the MyoCoach box by increase the dimension following the dimension of the raspberry pi. 

* The [armband](#armband)
* The Arduino board [casing](#casing)

## List of equipment
To design the MyoCoach, you will need :

* A 3D printer
* PLA type filament
* An Arduino UNO type board [link](https://store.arduino.cc/arduino-uno-rev3)
* A Raspberry pi [link](https://www.amazon.de/s?k=raspberry+pi+3+power&language=en_GB&adgrpid=81839545643&gclid=Cj0KCQiA0rSABhDlARIsAJtjfCchVfK8rE3ZXNvtey9SQwFffEQdmVJsKJW1rsvMP4mvpajCZgK8-k8aAh0_EALw_wcB&hvadid=394726547717&hvdev=c&hvlocphy=9056566&hvnetw=g&hvqmt=b&hvrand=8472442571307097874&hvtargid=kwd-301757869141&hydadcr=4926_1792628&tag=googdemozdesk-21&ref=pd_sl_533w78fssn_b)

* A female pin header strip [link](https://fr.farnell.com/samtec/ssq-110-03-f-s/connect-femelle-10-voies-1-rang/dp/2667433)
* A male pin header strip [link](https://fr.farnell.com/amp-te-connectivity/1-826629-0/barrette-droite-1-rangee-10voies/dp/3418376)
* A set of electronic cables [link](https://fr.farnell.com/pro-signal/psg-jws-65/jumper-wire-set-65pc/dp/2503764?MER=bn_level5_5NP_EngagementRecSingleItem_3)
* Self-tapping screws 8 x ∅2.2-L5 [link](https://www.visseriefixations.fr/catalog/product/view/id/38717)
* A strap with velcro and buckle [link](https://www.amazon.fr/gp/product/B07G9XFYM4/ref=ppx_yo_dt_b_asin_title_o05_s00?ie=UTF8&psc=1)


Tools :

* A Phillips screwdriver
* A soldering iron + soldering accessories
* A tube of glue type Glue

<a name="armband"></a>
## The ArmBand
The armband is the component of the MyoCoach that holds the two Ottobock EMG sensors (Ref 13E202) on the residual limb of the future prosthesis user. This armband is comfortable, inexpensive and facilitates the positioning of the sensors for the ortho-prosthetist.

### Printing of the Sensor Supports
The supports have been made with Fusion360 software. 

The file in .STL format is available in [this link](https://github.com/orthopus/01-myocoach/tree/master/src/hardware/casing)

![support print](./image/impression_support.png)

### armband assembly
Prepare the different elements: the printed material, the strap and the EMG sensor.

![assemblage_brassard](./image/assemblage_brassard.png)

* :one: Insert the strap into the side openings of the media.

> :bulb: The strap must be forced in.


* :two: Insert the Ottobock 13E202 sensor into the holder, taking care to force the strap between the holder and the sensor.

> :bulb: The sensor must go at the end of the mechanical stop in the holder.


### Adjustments and positioning
The design of the sensor holder and especially the design of the slot where the cable passes through offers a certain freedom of positioning between the two sensors. This freedom of movement allows the two EMG sensors to be correctly positioned above the user's muscle areas.

![reglage_du_brassard](./image/reglage_du_brassard.png)

<a name="casing"></a>
## The Casing
The MyoCoach's case allows EMG sensor data to be acquired with an Arduino card and transferred to a computer for visualisation. It also allows the Ottobock electrode connector format to be adapted to the MyoCoach casing.

### Casing printing
The casing of the Arduino Board has been made with Fusion360 software.

STL format files are available in [the link](https://github.com/orthopus/01-myocoach/tree/master/src/hardware/casing)

![impression_boitier](./image/impression_boitier.png)

### Preparation of the Arduino card
The main idea is to solder two female connectors (5-pin female pin header strips) to adapt to the female connectors of the Ottobock 13E202 sensors. The connectors are connected to the analogue ports A0 (EMG 0) and A1 (EMG 1) of the Arduino board.

The wiring diagram is as follows:

![arduino layout](./image/arduino_layout.png)

The result is as follows:

![soudure connecteur](./image/soudure_connecteur.png)

### Casing Assembly
Prepare the following items: the Arduino card, the two parts of the case, the female pin header strips and the 8 self-tapping screws.

![assemblage_boitier_1](./image/assemblage_boitier_1.png)

* :one: Insert the Arduino card into the case.

* :two: Screw in the 4 self-tapping screws to hold the Arduino card in the case.

![assemblage_boitier_2](./image/assemblage_boitier_2.png)

* :three: Using pliers, cut off the 2 outer pins of the snap-off strips.

* :four: To hold the connectors in place in the box, apply 2 drops of glue (Glue type) before placing the connectors in the box.

> :bulb: The cables are not shown in these illustrations but at this stage the connectors must be soldered.


![assemblage_boitier_3](./image/assemblage_boitier_3.png)

* :five: Close the housing

> :warning: Before closing the case, the connectors must be connected to the Arduino board (+5v, GND, EMG0 → A0, EMG1 → A1).

* :six: Turn the MyoCoach housing over and screw in the 4 self-tapping screws to hold the two housing covers in place.

### Electrode Connector
The connector of the Ottobock 13E202 electrodes is very specific.

![connecteur_electrode](./image/connecteur_electrode.png)


But a simple 3-pin header strip is used to interface between the electrodes and the connectors of the MyoCoach box.

![adpatateur_electrode](./image/adpatateur_electrode.png)


# Electrodes placement protocol
The primary function of the MyoCoach is to optimise electrode placement and find the right gain setting.

For this protocol, we use Ottobock electrodes (Ref 13E202).

This protocol is the result of a scientific publication from the University of Salford (UK).

> :bulb: Chadwell Alix, Kenney Laurence, Thies Sibylle, Galpin Adam, Head John (2016) The Reality of Myoelectric Prostheses: Understanding What Makes These Devices Difficult for Some Users to Control [url](https://www.frontiersin.org/articles/10.3389/fnbot.2016.00007/full)

This test protocol allows the placement of two electrodes which are useful for the use of a myoelectric prosthesis. We use two groups of wrist muscles to control the prosthesis:

* the **flexor muscles** of the wrist to **close the hand** of the prosthesis (1)
* the **extensor muscles** of the wrist to **open the hand** of the prosthesis (2)

![muscle_flechisseur_et_extenseur](./image/muscle_flechisseur_et_extenseur.png)

* :one: Equip an electrode with a pin header strip to make an adapter with the MyoCoach connector system.

![adpatateur_electrode](./image/adpatateur_electrode.png)

* :two: Adjust the electrode gain to a medium level between 3-4

To access the gain adjustment potentiometer of the Ottobock 13E202 sensor, it is not necessary to remove the sensor from the armband! Simply move it as shown below.

![acces_potentiometre](./image/acces_potentiometre.png)

* :three: Connect this electrode to the EMG 0 connector of the MyoCoach housing.

![connecteur_boitier](./image/connecteur_boitier.png)

* :four: Connect the MyoCoach box to power supply using a power cable connected to an electrical outlet.

* :five: Launch the MyoCoach application by scanning the flashcode, or enter the IP address of the hotspot with its port. Go to the Vizualisation Menu.
* :six: Hold the electrode on the user's muscle.

![maintien_electrode](./image/maintien_electrode.png)

An EMG electrode must be placed along and in the middle of the muscle fibre.

![myo_placement_muscle](./image/myo_placement_muscle.png)

* :seven: 7 Ask the user to repeatedly and regularly contract the muscle concerned by the electrode at a comfortable level, without too much muscle intensity. Note the level of the signal obtained.

![contraction_muscle_extenseur](./image/contraction_muscle_extenseur.png)

![contraction_muscle_flechisseur](./image/contraction_muscle_flechisseur.png)

* :eight: Then move the electrode in the 4 directions (up, down, left and right) from the starting position. The movement should be about half the width of the electrode (1 cm).

![deplacement_electrode](./image/deplacement_electrode.png)

* :nine: If the signal amplitude is greater at one of the new positions, repeat step :eight:, defining this new position as the starting point.

* :keycap_ten: The position with the maximum amplitude is then marked on the user's skin with a **pencil**.

![marquage_position_electrode](./image/marquage_position_electrode.png)


* Finally, the gain adjustment is defined so that the user can comfortably reach a signal level between 20 and 80% on the application's Signal Widget.

> :bulb: This protocol must be repeated for the second electrode.

### Connect Electrode to the box :

:one: Assemble the two electrodes on the armband. The armband offers several degrees of freedom to allow the electrodes to be positioned optimally on the user's arm. 

![vue_brassard](./image/vue_brassard.png)

:two: Connect the electrodes to the MyoCoach housing.

Once the electrodes have been connected and the ArmBand adjusted, the user is ready to practice using EMG sensors! :muscle:



# Boards Preparation

### Flash the arduino board
The Arduino board fulfils two roles:

* acquiring the signals from the EMG sensors on two analogue inputs
* sending this data to a raspberry  via the USB port by emulating a serial link.

<a >
    <img src="image/arduino_uno.PNG" alt="Logo" width="500" height="300">
  </a>

 We have used the online programming tool developed by Arduino. You can find help and information about this tool by following this link:
[Getting Started with Arduino Web Editor](https://create.arduino.cc/projecthub/Arduino_Genuino/getting-started-with-arduino-web-editor-on-various-platforms-4b3e4a?f=1)

We prefered to use the most basic arduino: **arduino uno**  but you can feel free to use another type of arduino...

### Flash the Raspberry pi SD card

<a >
    <img src="image/raspb.PNG" alt="Logo" width="500" height="300">
  </a>

The raspberry card needs a **SD card flashed by an operating system**. Several operating systems are available but for this project it will be necessary to use the **raspberry pi OS** ! And you can  take the aspberry pi OS  with the desktop option if your are not familiar to linux sytem. it will be preferable to use a class 10 SD card for more speed and fluidity of the operating system of the raspberry card.
The photo below is a raspberry pi 4 model B but you can use a lower model, either raspberry pi 3 model B or B+ will do ...
A powerful tutorial  is available [here](https://www.raspberrypi.org/documentation/installation/installing-images/).
Before that you can start the raspberry pi and install flask for python :

Install `flask` :
```bash
$ sudo apt-get install python3-flask
```

# Programmation


Don't be afraid you will not use to program anything again , just some commands to enter ;). Now you will really begin to build the system !

* :one:  **Create an account** on the online programming tool developed by Arduino: [Arduino Web Editor](https://create.arduino.cc)

* :two:  **Install the Arduino Web Editor** [plugin](https://create.arduino.cc/getting-started/plugin)

* :three: Importing the **myocoach.ino**  file into the online code editor

* :four: **Connecting the Arduino card to the computer you have already installed the arduino software

* :five: **Transfer the MyoCoach program to the Arduino card**. After doing all these steps, you can remove the arduino board from your pc and plug it into your raspberry pi like this picture above. 

<a >
    <img src="image/usb.PNG" alt="Logo" width="300" height="400">
  </a>

* :six: Considering that you have already flash your raspberry pi SD card following the tutorial we gave you previously , you can plug it on the raspberry pi and start it
After the  boot phase , **download the MyoCoach file project** from your raspberry pi by typing on the terminal of your raspberry pi  this command:

```bash
$ git clone https://github.com/AliouneDiouf/MyoCoach.git
```
Once you have downloaded the project file, place it somewhere you will remember. The code that launches the application is the python **app.py** file. Activate the SSH protocol by typing this command on the raspberry pi's terminal: 
```bash
$ sudo raspi-config
```
And then activate the SSH protocol. 

Well, you  must now make your rapsberry pi an access point to generate a hotspot at startup and  make your code automatic when booting  the raspberry pi.

* :seven: **Make your rapsberry pi an access point** 

We have used raspAP to install a WiFi hotspot in no time.  You can see their GItHub page in this [link] (https://raspap.com/). A tutorial is available there  but we think that it's not very powerful, that's why we give the steps to make your rapsberry pi an access point. 

<a >
    <img src="image/Capture4.PNG" alt="Logo" width="300" height="200">
  </a>


As always, it is advisable to start with a newly installed “clean” distribution. It avoids possible interference with other programs. 
Start by updating the system : 
```bash
$ sudo apt-get update
```
```bash
$ sudo apt-get upgrade
```
If you have a Raspberry Pi 3 or more recent, WiFi is integrated, with models 1 and 2 you will need a WiFi USB key recognized by Raspbian. If necessary, plug the key into one of the Raspberry Pi's USB ports.
To avoid having a “parasitic” configuration file, we will make a backup copy of the original WiFi configuration file **wpa_supplicant.conf**, then delete it.

```bash
$ sudo cp /etc/wpa_supplicant/wpa_supplicant.conf /etc/wpa_supplicant/wpa_supplicant.conf.org
```
Once this command is done you have copied your basic wifi configuration to the file directory /etc/wpa_supplicant/wpa_supplicant.conf.org, so you can retrieve it at any time.

Then you can delete the WiFi configuration file.

```bash
$ sudo  rm  /etc/wpa_supplicant/wpa_supplicant.conf
```

Install RaspAP from your device’s shell prompt (raspberry pi's terminal):
```bash
$ curl -sL https://install.raspap.com | bash
```


Your Raspberry Pi will display RaspAP and offer you folders for installing the RaspAP and Lighttpd programs. Unless you have good reasons to contradict him, answer him with: "Y". 

When you restarted the Raspberry Pi, RaspAP configured hostapd. The WiFi IP address of your AP (Access Point) is 10.3.141.0.

This is where you will access the wlan0 interface of the Raspberry Pi configured as an AP. RaspAP has also configured DHCP to distribute addresses between 10.3.141.50 and 10.3.141.255. When a device (PC, Raspberry Pi, smartphone, tablet, etc.) connects to this AP, DHCP will distribute an IP address between these two values.

To configure RaspAP, you access the administration interface via a web page, by connecting to the address of the AP, ie 10.3.141.1. This can be done either locally on the Raspberry Pi AP itself, or from another machine connected to the AP.

At the end of the installation, after restarting, the wireless network will be configured as an access point with the following default settings:

Management username: **admin**, Management password: **secret**, DHCP range: **10.3.141.50 to 10.3.141.255**, SSID:**raspi-webgui**,  Password: **ChangeMe**.
From a PC on windows you will see: 

<a>
    <img src="image/raspigui.PNG" alt="Logo" width="200" height="200">
  </a>
  
Now you have made rasberry pi an access point. You must connect to your rasberry pi from your pc by connecting to this wifi and using the SSH protocol. We suggest you use [putty](https://www.putty.org/). And use the 10.3.141.1 to access to the raspberry pi.  

<a >
    <img src="image/putty.PNG" alt="Logo" width="400" height="400">
  </a

The screenshot above shows exactly what you have to do with putty. If you don't do any changes the login of your raspberry pi  is : **pi** and the password: **raspberry**

* :eight: **Make the MyoCoach application running on boot**

You just have to modify the /etc/profile file by doing:

```bash
$ sudo nano /etc/profile
```
I remember you that the file that start the project is app.py.

Then added this at the bottom of the file: 
```bash
sudo python FILE PATH/app.py
```
Exit the file with CTRL + O , ENTER and CTRL + X.

IMPORTANT ! **YOU MUST REPLACE FILE PATH WITH THE ACTUAL PATH FROM WHERE YOU PUT THE PROJECT FILE.**


* :nine:  **Start the application**

Reboot the raspberry pi, make sure that you have well connected the EMG sensor to the arduino and that it is connected to the raspberry pi via the usb port.

From a pc , a tablet or a smartphone connect to the wifi hotspot of the raspberry pi and type this in a navigator : **10.3.141.1:5000**


<!-- USAGE EXAMPLES -->
## Usage

Here is a description of the MyoCoach interface.

![general_view](./image/recording2.gif)

### Menu : Vizualisation
This Menu allows you to visualize in real time the acquisition of EMG signals that will be use for the application.

* :one: Click on the **Vizualisation** Menu, both signals will be directly displayed.

![visualisation](./image/viz.PNG)
* :two: You can visualize in full screen each graph.

> :bulb: If during the use of the Vizualisation Menu, you encounter a problem (absence of EMG signals, blocking of the menus...), remember to reload the web page or go back to the main menu and do the previous steps again.

### Menu : Gaming
![gaming_page](./image/recording.gif)
In this menu you can choose between the different games.

* **Game 1**: You reach the Snake game.
![snake](./image/Capture1.PNG)

* A pulse from the **EMG 0** sensor that exceeds the threshold moves the snake **right**.
* A pulse from the **EMG 1** sensor that exceeds the threshold moves the snake **left**.
* The displacement of the snake is relative to the power of the pulse.


* **Game 2**: You reach the Flappy Bird game which is more difficult than the snake game
![Flappy](./image/Capture3.PNG)

* The bird does not fall. It maintains its height when the user does not control it
* A pulse from the **EMG 0** sensor that exceeds the threshold moves the bird **upwards**.
* A pulse from the **EMG 1** sensor that exceeds the threshold moves the bird **downwards**.
* The displacement of the bird is relative to the power of the pulse.

As you can see, the score is displayed as two gauges that represent the force deployed by the user. The threshold can be set when you reach the game page, it will determine the minimal force above which the game will react (eg: the bird going up or down, the snake going left or right).
The game play has been modified to better correspond to the use of EMG sensors but the graphics of the original game have been kept! :fire:

### Menu: About Us
In this menu you will find some information about our team and the background of the project.






<!-- CONTACT -->
## Contact

Alioune Badara Diouf  - badaradiouf101@gmail.com

[ LinkedIn] (www.linkedin.com/in/alioune-badara-diouf-019036120)



