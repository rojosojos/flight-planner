from kivy.app import App
from kivy.uix.widget import Widget


class AppInterface(Widget):
    pass


class FlightPlanning(App):
    def build(self):
        return AppInterface()

if __name__ == '__main__':
    FlightPlanning().run()