import kivy
from kivy.app import App
from kivy.core import window
from dodatki import clamp
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.core.window import Window

# class Odpad(Widget):
#     pass

class zwartoscApki(FloatLayout):
    smietnik = ObjectProperty(None)
    akt = 1
    smietniki = [["images/smietnikbrazowy.png", 0], ["images/smietnikniebieski.png", 0], ["images/smietnikszary.png", 0], ["images/smietnikzielony.png", 0], ["images/smietnikzolty.png", 0]]
    wynik = ObjectProperty(None)
    def lewy(self):
        self.akt -= 1
        self.wynik.text = str(self.smietniki[self.akt][1])
        self.akt = clamp(self.akt, self.smietniki)
        self.smietnik.source = self.smietniki[self.akt][0]
    def prawy(self):
        self.akt += 1
        self.akt = clamp(self.akt, self.smietniki)
        self.smietnik.source = self.smietniki[self.akt][0]
        self.wynik.text = str(self.smietniki[self.akt][1])
        print(self.akt)
    def dodaj(self):
        self.smietniki[self.akt][1] += 1
        self.wynik.text = str(self.smietniki[self.akt][1])

class ekoApp(App):
    def build(self):
        Window.clearcolor = (0.520, 0.520, 0.520, 0.5)
        return zwartoscApki()


if __name__ == "__main__":
    ekoApp().run()