from kivy.app import App
from controller import TimerController
from kivy.uix.boxlayout import BoxLayout

class CookingTimerApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical')
        controller = TimerController()
        root.add_widget(controller.view)
        return root

if __name__ == '__main__':
    CookingTimerApp().run()