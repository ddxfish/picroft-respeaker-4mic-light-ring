# Seeed Respeaker 4-mic Raspberry Pi light ring Support
# Animates your light ring during listen/think/speak phases
import threading
import time
import sys
from mycroft import MycroftSkill, intent_handler
try:
    from gpiozero import LED
    from .apa102pixel import PixelRing
except:
    self.log.warn("Respeaker - Failure importing gpiozero or apa102pixel.py")

#Because sometimes the light doesn't go off

class RespeakerSkill(MycroftSkill):
    def __init__(self):
        super().__init__()
        self.learning = True

    def initialize(self):
        self.ringstyle = self.settings.get('ringstyle')
        if self.ringstyle == "google" or self.ringstyle == "echo":
            self.log.debug("Respeaker - Ring Style options good")
        else:
            self.ringstyle = "google"
            self.log.info("Respeaker - Ring Style options bad - defaulting to Google")
        self.add_event('recognizer_loop:wakeword', self.handle_wakeword_started)
        self.add_event('recognizer_loop:record_end', self.handle_listener_ended)
        self.add_event('recognizer_loop:audio_output_start', self.handle_response_started)
        self.add_event('recognizer_loop:audio_output_end', self.handle_response_ended)
        try:
            self.pixel_ring = PixelRing(self.ringstyle)
            self.power = LED(5)
            self.power.on()
            self.pixel_ring.set_brightness(10)
            self.pixelringpresent = True
            self.pixel_ring.off()
            self.log.info("Respeaker - Yes Pixel Ring Support, SUCCESS")
        except:
            self.pixelringpresent = False
            self.log.warn("Respeaker - No Pixel Ring Support, FAILED")

    def ring_stop(self):
        self.pixel_ring.off()
        self.log.warn("pixel ring timed out")

    def handle_wakeword_started(self):
        if self.pixelringpresent:
            self.pixel_ring.wakeup()
            timer = threading.Timer(30.0, self.ring_stop)
            timer.start()
            self.log.warn("light ring timer began")

    def handle_listener_ended(self):
        if self.pixelringpresent:
            try:
                self.pixel_ring.think()
            except:
                self.log.warn("Respeaker - pixel ring command failed")

    def handle_response_started(self):
        if self.pixelringpresent:
            try:
                self.pixel_ring.speak()
            except:
                self.log.warn("Respeaker - pixel ring command failed")

    def handle_response_ended(self):
        if self.pixelringpresent:
            try:
                self.pixel_ring.off()
            except:
                self.log.warn("Respeaker - pixel ring command failed")

    @intent_handler('apa102.pattern.change.intent')
    def handle_apa102_pattern_change_intent(self, message):
        if self.pixelringpresent:
            pattern = message.data.get("pattern")
            if pattern.lower() == "echo" or pattern.lower() == "google":
                try:
                    self.pixel_ring.off()
                    self.pixel_ring = PixelRing(pattern)
                    self.log.info("Respeaker - style set to %s", str(pattern))
                except:
                    self.log.warn("Respeaker - pixel ring style switch failed")
            else:
                self.log.warn("Respeaker - style not valid, nothing changed")

def create_skill():
    return RespeakerSkill()
