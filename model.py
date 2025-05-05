class TimerModel:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration  # seconds
        self.remaining = duration
        self.running = False

    def tick(self):
        if self.running and self.remaining > 0:
            self.remaining -= 1

    def reset(self):
        self.remaining = self.duration
        self.running = False

    def start(self):
        self.running = True

    def pause(self):
        self.running = False