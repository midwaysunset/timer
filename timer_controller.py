from timer_model import TimerModel

class TimerController:
    def __init__(self):
        self.model = TimerModel()

    def get_presets(self):
        return self.model.get_presets()

    def add_preset(self, name, seconds):
        self.model.add_preset(name, seconds)