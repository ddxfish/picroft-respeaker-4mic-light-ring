This is a Mycroft skill for Raspberry Pi users who have the "Seeed Respeaker 4-mic Array for Raspberry Pi". The Respeaker 4-mic has a ring of LED lights that Mycroft core does not control. This skill makes the Seeed "pixel ring" on the Respeaker activate various patterns of lights.

Set up Seeed Respeaker 4-mic
https://wiki.seeedstudio.com/ReSpeaker_4_Mic_Array_for_Raspberry_Pi/
*git clone https://github.com/respeaker/seeed-voicecard.git
*cd to new seed directory
*sudo ./install.sh

Usage
Log into Mycroft.ai and set your preferred ring style. Currently it supports "google" or "echo", and nothing else.

Installation
*set up your picroft
*setup the respeaker and test it
*Enable SPI in raspi-config and reboot
*ssh to your picroft
*msm install https://github.com/ddxfish/picroft-respeaker-4mic-light-ring

Troubleshooting
*Tested on Raspberry Pi 4 (4GB) only
*Did you enable SPI in raspi-config and reboot?
*Get a fresh Picroft image, respeaker it, SPI and install this again

Credits
*apa102 https://github.com/tinue/apa102-pi
*apa102 library (c) Martin Erzberger 2016-2020
*apa102 license (also included) https://github.com/tinue/apa102-pi/blob/main/LICENSE
*samples and patterns: https://github.com/respeaker/seeed-voicecard.git
*Respeaker Pixel Ring: https://github.com/respeaker/pixel_ring