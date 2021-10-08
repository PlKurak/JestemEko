import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
import os
import sys
from kivy.core.window import Window
class zawartosc(FloatLayout):
    def quiz(self):
        os.system('python quiz.py')
        sys.exit()
    def smietniki(self):
        os.system('python nowy.py')
        sys.exit()


class menuApp(App):
        def build(self):
            Window.clearcolor = (0.520, 0.520, 0.520, 0.5)
            return zawartosc()
if __name__ == "__main__":
    menuApp().run()
