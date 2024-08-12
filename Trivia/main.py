from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder
from kivy.properties import StringProperty, ListProperty
from kivy.core.audio import SoundLoader
import random

# Importar las preguntas desde otro archivo
from preguntas import preguntas

# Cargar los archivos kv con la estructura de la interfaz
Builder.load_file("Mascaras/menu.kv")
Builder.load_file("Mascaras/Ajustes.kv")
Builder.load_file("Mascaras/Solitario.kv")
Builder.load_file("Mascaras/Preguntas.kv")
class WidAlfa(BoxLayout):
    def __init__(self, **kwargs):
        super(WidAlfa, self).__init__(**kwargs)
        self.music = {
            "menu_preguntas": "Musica/menu_music.mp3",
            "widstyle1": "Musica/widstyle1_music.mp3"
        }
        self.current_music = None
        self.music_player = None
        self.volume = 1.0  # Volumen inicial
        self.add_widget(Menu())
        self.play_music("menu_preguntas")

    def play_music(self, music_key):
        if self.music_player:
            self.music_player.stop()
        if music_key in self.music:
            self.music_player = SoundLoader.load(self.music[music_key])
            if self.music_player:
                self.music_player.loop = True
                self.music_player.volume = self.volume
                self.music_player.play()
            else:
                print(f"Error al cargar la música: {self.music[music_key]}")

    def set_volume(self, volume):
        self.volume = max(0.0, min(volume, 1.0))
        if self.music_player:
            self.music_player.volume = self.volume
        print(f"Volumen ajustado a: {self.volume}")

    def change_style(self, int_style, respuesta_correcta=None):
        self.clear_widgets()
        if int_style == 1:
            self.add_widget(Menu())
            self.play_music("menu_preguntas")
        elif int_style == 2:
            self.add_widget(Preguntas())
            self.play_music("menu_preguntas")
        elif int_style == 3:
            self.add_widget(WidStyle1())
            self.play_music("menu_preguntas")
        elif int_style == 4:
            self.add_widget(Ajustes(wid_alfa=self))
            self.play_music("menu_preguntas")
        elif int_style == 5:
            self.add_widget(Solitario())
            self.play_music("menu_preguntas")
        elif int_style == 6:
            self.add_widget(Correcto(respuesta_correcta=respuesta_correcta))
            self.play_music("menu_preguntas")
        elif int_style == 7:
            self.add_widget(Incorrecto(respuesta_correcta=respuesta_correcta))
            self.play_music("menu_preguntas")

    def next_question(self):
        self.clear_widgets()
        self.add_widget(Solitario())
        self.play_music("menu_preguntas")

class Solitario(BoxLayout):
    pregunta_actual = StringProperty('')
    opciones = ListProperty([])
    respuesta_correcta = StringProperty('')

    def __init__(self, **kwargs):
        super(Solitario, self).__init__(**kwargs)
        self.mostrar_pregunta()

    def mostrar_pregunta(self):
        pregunta = random.choice(preguntas)
        self.pregunta_actual = pregunta["pregunta"]
        self.respuesta_correcta = pregunta["respuesta_correcta"]
        self.opciones = pregunta["opciones"]
        random.shuffle(self.opciones)

    def verificar_respuesta(self, respuesta):
        app = App.get_running_app()
        if respuesta == self.respuesta_correcta:
            app.root_widget.change_style(6, self.respuesta_correcta)
        else:
            app.root_widget.change_style(7, self.respuesta_correcta)

class Correcto(BoxLayout):
    respuesta_correcta = StringProperty('')

    def __init__(self, respuesta_correcta='', **kwargs):
        super(Correcto, self).__init__(**kwargs)
        self.respuesta_correcta = respuesta_correcta
        app = App.get_running_app()
        puntaje_actual = int(app.puntaje)
        app.puntaje = str(puntaje_actual + 1)
        print(f"Puntaje actualizado: {app.puntaje}")

class Incorrecto(BoxLayout):
    respuesta_correcta = StringProperty('')

    def __init__(self, respuesta_correcta='', **kwargs):
        super(Incorrecto, self).__init__(**kwargs)
        self.respuesta_correcta = respuesta_correcta
        app = App.get_running_app()
        puntaje_actual = int(app.puntaje)
        app.puntaje = str(puntaje_actual - 1)
        print(f"Puntaje actualizado: {app.puntaje}")

class Menu(BoxLayout):
    pass

class Preguntas(BoxLayout):
    pass

class WidStyle1(BoxLayout):
    pass

class Ajustes(BoxLayout):
    def __init__(self, wid_alfa=None, **kwargs):
        super(Ajustes, self).__init__(**kwargs)
        self.wid_alfa = wid_alfa

    def adjust_volume(self, volume):
        if self.wid_alfa and hasattr(self.wid_alfa, 'set_volume'):
            self.wid_alfa.set_volume(volume)

class MainApp(App):
    puntaje = StringProperty('0')

    def build(self):
        self.title = 'Trivia'
        self.root_widget = WidAlfa()
        return self.root_widget

    def next_question(self):
        if hasattr(self.root_widget, 'next_question'):
            self.root_widget.next_question()
        else:
            print("El método next_question no está disponible en root_widget.")

if __name__ == '__main__':
    MainApp().run()
