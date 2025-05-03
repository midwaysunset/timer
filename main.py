from kivy.app import App
from timer_view import TimerScreen
from timer_controller import TimerController

class CookingTimerApp(App):
    def build(self):
        controller = TimerController()
        return TimerScreen(controller)

if __name__ == '__main__':
    CookingTimerApp().run()