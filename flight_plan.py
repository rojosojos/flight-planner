from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder


Builder.load_file("flight_plan.kv")

class AppInterface(BoxLayout):
    pass


class FlightPlanning(App):
    def build(self):
        return AppInterface()

if __name__ == '__main__':
    FlightPlanning().run()