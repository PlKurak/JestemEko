import kivy
from kivy import app
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button 
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
import random
import time
from kivy.core.window import Window

class zawartoscQuiz(FloatLayout):
    # tutaj importujemy id z pliku kv by odnieść się do przycisków i wysłać tekst
    pytanie = ObjectProperty(None)
    odp = ObjectProperty(None)
    start = ObjectProperty(None)
    error = ObjectProperty(None)
    odpw = ""
    # twoje dane
    i = 0
    punkty = 0
    t = [["Od czego jest niebieski śmietnik? \n A: Papier \n B: Plastik \n C: Odpady bio \n D: Odpady mieszane" ,"a"],
    ["Co jest objęte ochroną w rzece Rawce? \n A: jelenie \n B: bobry \n C: sarny \n D: karpie ","b"],
    ['Kiedy odbywa się światowa akcja "Sprzątanie świata" \n A: drugi tydzień czerwca \n B: trzeci weekend września \n C: pierwszy miesiac stycznia \n D: czwarty weekend grudnia ',"b"],
    ["Ile obecnie w Polsce znajduje się parków narodowych? \n A: 27 \n B: 17 \n C: 22  \n D: 23","d"],
    ["Światowy Dzień Ochrony środowiska obchodzimy: \n A: 12 września \n B: 15 maja \n C: 5 czerwca \n D: 8 października", "c"],
    ["W wyniku czego zwiększa się efekt cieplarniany? \n A: wycinania lasów \n B: jedzenia lodów w lato \n C: strojenia choinek na święta \n D: kąpania się w morzu ","a"],
    ["Odnawialne źródło energii to: \n A: gaz ziemny \n B: ropa noftowa \n C: węgiel brunatny \n D: energia słoneczna ","d"],
    ["Nieodnawialne źródło energii to \n A: energia słoneczna \n B: wiatr \n C: ropa naftowa \n D: woda", "c"]]
    print()
    m = 4
    # nowa tablica z wybranymi zadaniami
    table = []
    while i < 5:
        z = random.randint(0, m)
        # dodaje do tablicy zadania
        table.append(t[z][0])
        table.append(t[z][1])
        # usuwamy stare zadania z starej tablicy
        del t[z]
        
        print(t)
        i += 1
        m -= 1
    print(table)
    i = 0
    # funkcja rozpoczynająca skrypt, wykonana po naciśnięciu przycisku
    def losu(self):
        self.odp.disabled = False
        self.start.disabled = True
        # zmiana przezroczystości nowych i starych przycisków
        self.odp.opacity = 1
        self.start.opacity = 0
        # wypisanie pytania 
        self.pytanie.text = self.table[self.i]
    print(table)
    # funkcja działająca po naciśnięciu przycisku
    def odpowiedz(self, instance):
        if self.i == 10:
            self.koniec()
        else:
            self.i += 1        
            # najpierw zczytuje tekst z naciśniętego przycisku
            self.odpw = str(instance.text)
            # potem porównuje go z odpowiedzią z tablicy
            if(self.odpw == self.table[self.i]):
                # jeśli są takie same to dodaje 10 punktów
                self.punkty += 10
            elif(self.odpw != self.table[self.i]):
                # w teori jeśli nie jest równa to wypisuje błąd
                self.error.text = "Źle, poprawna odpowiedź to " + self.table[self.i]
                time.sleep(0.1)
            # następnie dodaje do i 1 by móc wyświetlić następne pytanie
            self.i += 1
        if self.i == 10:
            self.koniec()
        else:
            # zmienia stare pytanie na nowe
            self.pytanie.text = self.table[self.i]
    def koniec(self):
        self.pytanie.text = "Gratulacje"
        self.odp.opacity = 0
        self.odp.disabled = True
        self.error.text = "Zdobyłeś " + str(self.punkty) + " punktów"

    # wypisuje długość tablicy


# definiujemy naszą aplikacje
class quizzApp(App):
        def build(self):
            Window.clearcolor = (0.520, 0.520, 0.520, 0.5)
            return zawartoscQuiz()

# uruchamia aplikacje
if __name__ == "__main__":
    quizzApp().run()