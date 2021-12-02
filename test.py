import threading

class RespeakerSkill():
    def ring_stop(self):
        print("ring stopped")

    def handle_wakeword_started(self):
        self.timer = threading.Timer(3.0, self.ring_stop)
        self.timer.start()
        print("starting timer")

if __name__ == "__main__" :
    test1 = RespeakerSkill()
    test1.handle_wakeword_started()
