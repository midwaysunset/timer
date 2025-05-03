from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.clock import Clock

class TimerScreen(BoxLayout):
    def __init__(self, controller, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.controller = controller
        self.timer_running = False
        self.time_left = 0

        self.label = Label(text="00:00", font_size=48)
        self.add_widget(self.label)

        self.start_btn = Button(text="Старт", size_hint=(1, 0.2))
        self.start_btn.bind(on_press=self.start_timer)
        self.add_widget(self.start_btn)

        self.input_name = TextInput(hint_text='Название пресета')
        self.add_widget(self.input_name)

        self.input_time = TextInput(hint_text='Время (сек)', input_filter='int')
        self.add_widget(self.input_time)

        self.save_btn = Button(text="Сохранить пресет")
        self.save_btn.bind(on_press=self.save_preset)
        self.add_widget(self.save_btn)

        self.presets_box = BoxLayout(orientation='vertical', size_hint_y=None)
        self.add_widget(self.presets_box)

        self.load_presets()

    def update_label(self, dt):
        if self.time_left > 0:
            self.time_left -= 1
            minutes = self.time_left // 60
            seconds = self.time_left % 60
            self.label.text = f"{minutes:02}:{seconds:02}"
        else:
            self.label.text = "Готово!"
            self.timer_event.cancel()

    def start_timer(self, instance):
        if not self.timer_running:
            self.time_left = int(self.input_time.text or 0)
            self.timer_event = Clock.schedule_interval(self.update_label, 1)
            self.timer_running = True

    def save_preset(self, instance):
        name = self.input_name.text
        time_sec = int(self.input_time.text or 0)
        self.controller.add_preset(name, time_sec)
        self.load_presets()

    def load_presets(self):
        self.presets_box.clear_widgets()
        presets = self.controller.get_presets()
        for name, time_sec in presets.items():
            btn = Button(text=f"{name} - {time_sec} сек")
            btn.bind(on_press=lambda inst, t=time_sec: self.set_timer(t))
            self.presets_box.add_widget(btn)

    def set_timer(self, seconds):
        self.input_time.text = str(seconds)