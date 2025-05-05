from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class TimerView(BoxLayout):
    def __init__(self, controller, timer_index, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.controller = controller
        self.timer_index = timer_index

        self.label = Label(text='00:00', font_size=32)
        self.name_input = TextInput(hint_text='Название пресета', multiline=False)
        self.time_input = TextInput(hint_text='Время (сек)', multiline=False, input_filter='int')

        self.start_button = Button(text='Старт')
        self.pause_button = Button(text='Пауза')
        self.reset_button = Button(text='Сброс')

        self.start_button.bind(on_press=self.on_start)
        self.pause_button.bind(on_press=self.on_pause)
        self.reset_button.bind(on_press=self.on_reset)

        self.add_widget(self.name_input)
        self.add_widget(self.time_input)
        self.add_widget(self.label)
        self.add_widget(self.start_button)
        self.add_widget(self.pause_button)
        self.add_widget(self.reset_button)

    def update_display(self, seconds):
        mins, secs = divmod(seconds, 60)
        self.label.text = f'{mins:02}:{secs:02}'

    def on_start(self, _):
        name = self.name_input.text
        duration = int(self.time_input.text or '0')
        self.controller.start_timer(self.timer_index, name, duration)

    def on_pause(self, _):
        self.controller.pause_timer(self.timer_index)

    def on_reset(self, _):
        self.controller.reset_timer(self.timer_index)