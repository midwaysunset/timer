from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from model import TimerModel
from view import TimerView

class TimerController:
    def __init__(self):
        self.models = [None] * 3
        self.views = []
        self.view = BoxLayout(orientation='horizontal')

        for i in range(3):
            model = TimerModel(f"Таймер {i+1}", 0)
            self.models[i] = model
            timer_view = TimerView(self, i)
            self.views.append(timer_view)
            self.view.add_widget(timer_view)

        Clock.schedule_interval(self.update_timers, 1)

    def start_timer(self, index, name, duration):
        model = self.models[index]
        model.name = name
        model.duration = duration
        model.remaining = duration
        model.start()
        self.views[index].update_display(model.remaining)

    def pause_timer(self, index):
        self.models[index].pause()

    def reset_timer(self, index):
        self.models[index].reset()
        self.views[index].update_display(self.models[index].remaining)

    def update_timers(self, dt):
        for i in range(3):
            model = self.models[i]
            if model.running:
                model.tick()
                self.views[i].update_display(model.remaining)