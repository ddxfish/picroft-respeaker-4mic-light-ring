# Seeed Respeaker 4-mic Raspberry Pi light ring Support
# Animates your light ring during listen/think/speak phases

from mycroft import MycroftSkill, intent_handler
try:
    from gpiozero import LED
    from .apa102pixel import PixelRing
except:
    self.log.warn("Respeaker - Failure importing gpiozero or apa102pixel.py")

class RespeakerSkill(MycroftSkill):
    def __init__(self):
        super().__init__()
        self.learning = True

    def initialize(self):
        self.ringstyle = self.settings.get('ringstyle').lower()
        if self.ringstyle == "google" or self.ringstyle == "echo":
            self.log.debug("Respeaker - Ring Style options good")
        else:
            self.ringstyle = "google"
            self.log.info("Respeaker - Ring Style options bad - defaulting to Google")
        self.add_event('recognizer_loop:wakeword', self.handle_wakeword_started)
        self.add_event('recognizer_loop:record_end', self.handle_listener_ended)
        self.add_event('recognizer_loop:audio_output_start', self.handle_response_started)
        self.add_event('recognizer_loop:audio_output_end', self.handle_response_ended)
        self.add_event('mycroft.skills.settings.update', self.handle_settings_updated)
        try:
            self.pixel_ring = PixelRing(self.ringstyle)
            self.power = LED(5)
            self.power.on()
            self.pixel_ring.set_brightness(10)
            self.pixelringpresent = True
            self.log.info("Respeaker - Yes Pixel Ring Support - SUCCESS")
        except:
            self.pixelringpresent = False
            self.log.warn("Respeaker - No Pixel Ring Support - FAILED")


    def handle_wakeword_started(self):
        if self.pixelringpresent:
            try:
                self.pixel_ring.wakeup()
            except:
                self.log.warn("Respeaker - pixel ring command failed")

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
            pattern = message.data.get("pattern").lower()
            if pattern == "echo" or pattern == "google":
                try:
                    self.pixel_ring.off()
                    self.pixel_ring = PixelRing(pattern)
                    self.log.info("Respeaker - style set to %s", str(pattern))
                except:
                    self.log.warn("Respeaker - pixel ring style switch failed")
            else:
                self.log.warn("Respeaker - style not valid, nothing changed")
