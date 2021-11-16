# Mycroft - Respeaker 4-mic Light Ring Control

This is a Mycroft skill for Raspberry Pi users who have the "Seeed Respeaker 4-mic Array for Raspberry Pi". The Respeaker 4-mic has a ring of LED lights that Mycroft core does not control. This skill makes the Seeed "pixel ring" on the Respeaker activate various patterns of lights when listening, thinking, or speaking.

## Usage
This plugin is automatic. It lights up when mycroft is listening, thinking, or talking. You can change the ring pattern permanently in your Mycroft Setting page, or temporarily with a command.<br>
**Hey Mycroft! Change the ring pattern to (echo|google)**

## Installation
* set up your picroft
* setup the respeaker and test it
* Enable SPI in raspi-config and reboot
* ssh to your picroft
* msm install https://github.com/ddxfish/picroft-respeaker-4mic-light-ring
* All done!

### Seeed Respeaker 4-mic for Raspberry Pi
https://wiki.seeedstudio.com/ReSpeaker_4_Mic_Array_for_Raspberry_Pi/
```
git clone https://github.com/respeaker/seeed-voicecard.git
cd seeed-voicecard
sudo ./install.sh
```

## Troubleshooting
* Do you have a Pixel Ring installed? (rpi 4-mic hat)
* Tested on Raspberry Pi 4 (4GB) running Picroft v20.08
* Did you enable SPI in raspi-config and reboot?
* Test your Respeaker mic is working in Mycroft
* I had to run the Respeaker install.sh twice as instructed
* Get a fresh Picroft image, respeaker it, SPI and install this again

## Known Bugs
* Pixel ring stops when Mycroft's response ends. No response, no ring stop.

## Credits
* apa102 https://github.com/tinue/apa102-pi
* apa102 library (c) Martin Erzberger 2016-2020
* apa102 license (also included) https://github.com/tinue/apa102-pi/blob/main/LICENSE
* Respeaker Device: https://github.com/respeaker/seeed-voicecard.git
* Respeaker Pixel Ring Code: https://github.com/respeaker/pixel_ring
