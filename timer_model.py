import json
import os

class TimerModel:
    def __init__(self):
        self.presets_file = 'presets.json'
        self.presets = self.load_presets()

    def load_presets(self):
        if not os.path.exists(self.presets_file):
            return {}
        with open(self.presets_file, 'r') as f:
            return json.load(f)

    def save_presets(self):
        with open(self.presets_file, 'w') as f:
            json.dump(self.presets, f)

    def add_preset(self, name, time_sec):
        self.presets[name] = time_sec
        self.save_presets()

    def get_presets(self):
        return self.presets