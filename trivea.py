import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder
from kivy.properties import StringProperty, ListProperty

# Definir las preguntas y respuestas
preguntas = [
        {
        "pregunta": "¿Cuál es el ácido presente en las naranjas?",
        "opciones": ["Ácido cítrico", "Ácido acético", "Ácido sulfúrico", "Ácido clorhídrico"],
        "respuesta_correcta": "Ácido cítrico / Ácido cítrico"
    },
    {
        "pregunta": "¿Qué gas necesitan las plantas para realizar la fotosíntesis?",
        "opciones": ["Dióxido de carbono", "Nitrógeno", "Oxígeno", "Hidrógeno"],
        "respuesta_correcta": "Dióxido de carbono / CO2"
    },
    {
        "pregunta": "¿Cuál es el hueso más largo del cuerpo humano?",
        "opciones": ["Fémur", "Húmero", "Tibia", "Radio"],
        "respuesta_correcta": "Fémur"
    },
    {
        "pregunta": "¿Cuál es el planeta más grande del sistema solar?",
        "opciones": ["Júpiter", "Saturno", "Neptuno", "Urano"],
        "respuesta_correcta": "Júpiter"
    },
    {
        "pregunta": "¿Cuál es la montaña más alta del mundo?",
        "opciones": ["Monte Everest", "Monte Kilimanjaro", "Monte Aconcagua", "Monte McKinley"],
        "respuesta_correcta": "Monte Everest"
    },
    {
        "pregunta": "¿Cuál es el metal más abundante en la corteza terrestre?",
        "opciones": ["Aluminio", "Hierro", "Cobre", "Plomo"],
        "respuesta_correcta": "Aluminio"
    },
    {
        "pregunta": "¿Cuál es el río más largo del mundo?",
        "opciones": ["Río Amazonas", "Río Nilo", "Río Yangtsé", "Río Misisipi"],
        "respuesta_correcta": "Río Amazonas"
    },
    {
        "pregunta": "¿Cuál es la capital de Australia?",
        "opciones": ["Sídney", "Melbourne", "Brisbane", "Camberra"],
        "respuesta_correcta": "Camberra"
    },
    {
        "pregunta": "¿Quién escribió la novela 'Cien años de soledad'?",
        "opciones": ["Gabriel García Márquez", "Mario Vargas Llosa", "Julio Cortázar", "Jorge Luis Borges"],
        "respuesta_correcta": "Gabriel García Márquez"
    },
    {
        "pregunta": "¿Cuál es la capital de Francia?",
        "opciones": ["Londres", "Madrid", "París", "Roma"],
        "respuesta_correcta": "París"
    },
    {
        "pregunta": "¿Cuál es el proceso por el cual las plantas producen su propio alimento?",
        "opciones": ["Fotosíntesis", "Respiración", "Digestión", "Germinación"],
        "respuesta_correcta": "Fotosíntesis"
    },
    {
        "pregunta": "¿Quién pintó la 'Mona Lisa'?",
        "opciones": ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Rembrandt"],
        "respuesta_correcta": "Leonardo da Vinci"
    },
    {
        "pregunta": "¿Cuál es el hueso más pequeño del cuerpo humano?",
        "opciones": ["Estribo", "Martillo", "Yunque", "Escápula"],
        "respuesta_correcta": "Estribo"
    },
    {
        "pregunta": "¿Cuál es el océano más grande del mundo?",
        "opciones": ["Océano Atlántico", "Océano Índico", "Océano Pacífico", "Océano Ártico"],
        "respuesta_correcta": "Océano Pacífico"
    },
    {
        "pregunta": "¿Qué unidad se utiliza para medir la electricidad?",
        "opciones": ["Voltios", "Watts", "Amperios", "Julios"],
        "respuesta_correcta": "Amperios"
    },
    {
        "pregunta": "¿En qué año llegó el hombre a la Luna por primera vez?",
        "opciones": ["1969", "1972", "1965", "1975"],
        "respuesta_correcta": "1969"
    },
    {
        "pregunta": "¿Cuál es el país más grande del mundo por área terrestre?",
        "opciones": ["Rusia", "Canadá", "China", "Estados Unidos"],
        "respuesta_correcta": "Rusia"
    },
    {
        "pregunta": "¿Quién escribió 'Don Quijote de la Mancha'?",
        "opciones": ["Miguel de Cervantes", "Lope de Vega", "Federico García Lorca", "Garcilaso de la Vega"],
        "respuesta_correcta": "Miguel de Cervantes"
    },
    {
        "pregunta": "¿Cuál es la flor típica de Japón conocida por su belleza y simbolismo?",
        "opciones": ["Rosa", "Lirio", "Tulipán", "Cerezo"],
        "respuesta_correcta": "Cerezo / Flor del cerezo"
    },
    {
        "pregunta": "¿En qué ciudad se encuentra la Torre Eiffel?",
        "opciones": ["Berlín", "Londres", "París", "Roma"],
        "respuesta_correcta": "París"
    },
    {
        "pregunta": "¿Cuál es la unidad fundamental de la vida?",
        "opciones": ["Átomo", "Célula", "Molécula", "Protón"],
        "respuesta_correcta": "Célula"
    },
    {
        "pregunta": "¿Cuál es la fórmula química del agua?",
        "opciones": ["H2O2", "CO2", "H2O", "NaCl"],
        "respuesta_correcta": "H2O"
    },
    {
        "pregunta": "¿Qué planeta es conocido como el planeta rojo?",
        "opciones": ["Marte", "Júpiter", "Saturno", "Venus"],
        "respuesta_correcta": "Marte"
    },
    {
        "pregunta": "¿Quién escribió 'Don Quijote de la Mancha'?",
        "opciones": ["Miguel de Cervantes", "Gabriel García Márquez", "Jorge Luis Borges", "Pablo Neruda"],
        "respuesta_correcta": "Miguel de Cervantes"
    },
    {
        "pregunta": "¿Cuál es el océano más grande del mundo?",
        "opciones": ["Atlántico", "Índico", "Pacífico", "Ártico"],
        "respuesta_correcta": "Pacífico"
    },
    {
        "pregunta": "¿En qué año llegó el hombre a la luna?",
        "opciones": ["1965", "1969", "1971", "1975"],
        "respuesta_correcta": "1969"
    },
    {
        "pregunta": "¿Cuál es el elemento químico más abundante en la corteza terrestre?",
        "opciones": ["Hierro", "Silicio", "Oxígeno", "Aluminio"],
        "respuesta_correcta": "Oxígeno"
    },
    {
        "pregunta": "¿Quién pintó la Mona Lisa?",
        "opciones": ["Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso", "Claude Monet"],
        "respuesta_correcta": "Leonardo da Vinci"
    },
    {
        "pregunta": "¿Cuál es el río más largo del mundo?",
        "opciones": ["Nilo", "Amazonas", "Yangtsé", "Misisipi"],
        "respuesta_correcta": "Amazonas"
    },
    {
        "pregunta": "¿Cuál es el país con la mayor población del mundo?",
        "opciones": ["India", "Estados Unidos", "Indonesia", "China"],
        "respuesta_correcta": "China"
    },
    {
        "pregunta": "¿Cuál es el metal más liviano?",
        "opciones": ["Hierro", "Aluminio", "Litio", "Plata"],
        "respuesta_correcta": "Litio"
    },
    {
        "pregunta": "¿Quién fue el primer presidente de los Estados Unidos?",
        "opciones": ["Abraham Lincoln", "Thomas Jefferson", "John Adams", "George Washington"],
        "respuesta_correcta": "George Washington"
    },
    {
        "pregunta": "¿Cuál es el idioma más hablado en el mundo?",
        "opciones": ["Inglés", "Español", "Chino mandarín", "Hindú"],
        "respuesta_correcta": "Chino mandarín"
    },
    {
        "pregunta": "¿Cuál es el planeta más grande del sistema solar?",
        "opciones": ["Saturno", "Júpiter", "Neptuno", "Urano"],
        "respuesta_correcta": "Júpiter"
    },
    {
        "pregunta": "¿Quién desarrolló la teoría de la relatividad?",
        "opciones": ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Nikola Tesla"],
        "respuesta_correcta": "Albert Einstein"
    },
    {
        "pregunta": "¿Cuál es el país más grande del mundo en términos de superficie?",
        "opciones": ["Canadá", "China", "Rusia", "Estados Unidos"],
        "respuesta_correcta": "Rusia"
    },
    {
        "pregunta": "¿Cuál es el animal terrestre más rápido?",
        "opciones": ["León", "Guepardo", "Antílope", "Tigre"],
        "respuesta_correcta": "Guepardo"
    },
    {
        "pregunta": "¿Cuál es la capital de Australia?",
        "opciones": ["Sídney", "Melbourne", "Canberra", "Brisbane"],
        "respuesta_correcta": "Canberra"
    },
    {
        "pregunta": "¿Cuál es el órgano más grande del cuerpo humano?",
        "opciones": ["Hígado", "Pulmones", "Piel", "Corazón"],
        "respuesta_correcta": "Piel"
    },
    {
        "pregunta": "¿Qué gas es esencial para la respiración?",
        "opciones": ["Dióxido de carbono", "Oxígeno", "Hidrógeno", "Nitrógeno"],
        "respuesta_correcta": "Oxígeno"
    }
]

# Cargar el archivo kv con la estructura de la interfaz
Builder.load_string('''
<WidAlfa>:
    orientation: 'vertical'
    pregunta_actual: ''
    opciones: []
    respuesta_correcta: ''
    puntaje: ''  # Añadido para mantener un puntaje inicial

    BoxLayout:
        size_hint_y: 0.1  # 10% del tamaño vertical total
        canvas.before:
            Color:
                rgba: 1, 0, 0, 1  # Color rojo de fondo
            Rectangle:
                pos: self.pos
                size: self.size

        Label:
            text: " " + str(root.puntaje)  # Mostrar el puntaje actual aquí
            size_hint: None, None
            size: self.texture_size[0] + 20, self.texture_size[1] + 20
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            color: 1, 1, 1, 1  # Texto blanco
            markup: True
            font_size: '25sp'

    BoxLayout:
        size_hint_y: 0.5  # 50% del tamaño vertical total
        orientation: 'vertical'
        canvas.before:
            Color:
                rgba: 1, 0, 0, 1  # Color rojo de fondo
            Rectangle:
                pos: self.pos
                size: self.size

        BoxLayout:
            size_hint_y: 0.2  # 20% del tamaño vertical total
            canvas.before:
                Color:
                    rgba: 1, 0, 0, 1  # Color rojo de fondo
                Rectangle:
                    pos: self.pos
                    size: self.size

        BoxLayout:
            size_hint_y: 0.3  # 30% del tamaño vertical total
            orientation: 'vertical'
            canvas.before:
                Color:
                    rgba: 1, 0, 0, 1  # Color rojo de fondo
                Rectangle:
                    pos: self.x + self.width * 0.1, self.y + self.height * 0.1
                    size: self.width * 0.8, self.height * 0.8

            Label:
                text: root.pregunta_actual  # Mostrar la pregunta actual aquí
                size_hint: None, None
                size: self.texture_size[0] + 20, self.texture_size[1] + 20  # Ajustar tamaño al contenido más margen
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}  # Centrar el Label en su contenedor
                color: 1, 1, 1, 1  # Texto blanco
                markup: True  # Activar markup para usar etiquetas de texto enriquecido
                font_size: '25sp'  # Tamaño de fuente en escala de puntos

        BoxLayout:
            size_hint_y: 0.5  # 50% del tamaño vertical total
            canvas.before:
                Color:
                    rgba: 1, 0, 0, 1  # Color rojo de fondo
                Rectangle:
                    pos: self.pos
                    size: self.size

    BoxLayout:
        size_hint_y: 0.2  # 20% del tamaño vertical total
        BoxLayout:
            orientation: 'horizontal'
            size_hint_x: 0.5  # 50% del tamaño horizontal de la sección
            canvas.before:
                Color:
                    rgba: 0, 0, 1, 1  # Azul
                Rectangle:
                    pos: self.pos
                    size: self.size

            Button:
                text: root.opciones[0] if root.opciones else ''
                halign: 'center'  # Alineación horizontal centrada
                valign: 'middle'   # Alineación vertical centrada
                text_size: self.size  # Tamaño del texto ajustado al tamaño del botón
                on_release: root.verificar_respuesta(self.text)

            Button:
                text: root.opciones[1] if root.opciones else ''
                halign: 'center'  # Alineación horizontal centrada
                valign: 'middle'   # Alineación vertical centrada
                text_size: self.size  # Tamaño del texto ajustado al tamaño del botón
                on_release: root.verificar_respuesta(self.text)

    BoxLayout:
        size_hint_y: 0.2  # 20% del tamaño vertical total
        BoxLayout:
            orientation: 'horizontal'
            size_hint_x: 0.5  # 50% del tamaño horizontal de la sección
            canvas.before:
                Color:
                    rgba: 0, 1, 0, 1  # Verde
                Rectangle:
                    pos: self.pos
                    size: self.size

            Button:
                text: root.opciones[2] if root.opciones else ''
                halign: 'center'  # Alineación horizontal centrada
                valign: 'middle'   # Alineación vertical centrada
                text_size: self.size  # Tamaño del texto ajustado al tamaño del botón
                on_release: root.verificar_respuesta(self.text)

            Button:
                text: root.opciones[3] if root.opciones else ''
                halign: 'center'  # Alineación horizontal centrada
                valign: 'middle'   # Alineación vertical centrada
                text_size: self.size  # Tamaño del texto ajustado al tamaño del botón
                on_release: root.verificar_respuesta(self.text)

<WidStyle>:
    orientation: 'vertical'
    BoxLayout:
        orientation: 'vertical'
        canvas.before:
            Color:
                rgba: 0, 1, 0, 1  # Verde
            Rectangle:
                pos: self.pos
                size: self.size
        Label:
            text: 'Correcto: ' + root.respuesta_correcta  # Mostrar la respuesta correcta
            font_size: 35
            size_hint: None, None
            size: self.texture_size[0] + 20, self.texture_size[1] + 20
            pos_hint: {'center_x': 0.5, 'top': 1}
            valign: 'top'
            color: 0, 0, 0, 1  # Texto negro
            markup: True
        Widget:  # Espaciador para empujar el botón hacia abajo
            size_hint_y: 0.7
        Button:
            text: 'Siguiente'
            size_hint: None, None
            size: root.width * 0.2, root.height * 0.1
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}  # Botón centrado en el medio
            on_release: app.next_question()

<WidStyle1>:
    orientation: 'vertical'
    BoxLayout:
        orientation: 'vertical'
        canvas.before:
            Color:
                rgba: 1, 0, 0, 1  # Rojo
            Rectangle:
                pos: self.pos
                size: self.size
        Label:
            text: 'Incorrecto: ' + root.respuesta_correcta  # Mostrar la respuesta correcta
            font_size: 35
            size_hint: None, None
            size: self.texture_size[0] + 20, self.texture_size[1] + 20
            pos_hint: {'center_x': 0.5, 'top': 1}
            valign: 'top'
            color: 1, 1, 1, 1  # Texto blanco
            markup: True
        Widget:  # Espaciador para empujar el botón hacia abajo
            size_hint_y: 0.7
        Button:
            text: 'Siguiente'
            size_hint: None, None
            size: root.width * 0.2, root.height * 0.1
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}  # Botón centrado en el medio
            on_release: app.next_question()

<WidStyle2>:

''')

class WidAlfa(BoxLayout):
    pregunta_actual = StringProperty('')
    opciones = ListProperty([])
    respuesta_correcta = StringProperty('')

    def __init__(self, **kwargs):
        super(WidAlfa, self).__init__(**kwargs)
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
            app.change_style(1)
        else:
            app.change_style(2)

class WidStyle(BoxLayout):
    respuesta_correcta = StringProperty('')

class WidStyle1(BoxLayout):
    respuesta_correcta = StringProperty('')

class WidStyle2(BoxLayout):
    pass

class MainApp(App):
    def build(self):
        self.root_widget = BoxLayout(orientation='vertical')
        self.wid_alfa = WidAlfa()
        self.root_widget.add_widget(self.wid_alfa)
        return self.root_widget

    def change_style(self, style):
        self.root_widget.clear_widgets()
        if style == 1:
            wid_style = WidStyle(respuesta_correcta=self.wid_alfa.respuesta_correcta)
        elif style == 2:
            wid_style = WidStyle1(respuesta_correcta=self.wid_alfa.respuesta_correcta)
        else:
            wid_style = WidStyle2()
        self.root_widget.add_widget(wid_style)

    def next_question(self):
        self.root_widget.clear_widgets()
        self.wid_alfa = WidAlfa()
        self.root_widget.add_widget(self.wid_alfa)

if __name__ == '__main__':
    MainApp().run()
