from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.image import Image

import csv
from kivy.uix.filechooser import FileChooserIconView

class PantallaImportarCSV(Screen):
    def __init__(self, **kwargs):
        super(PantallaImportarCSV, self).__init__(**kwargs)

        background = Image(source='background_CSV.jpg', allow_stretch=True)

        self.add_widget(background)

        self.filechooser = FileChooserIconView()
        self.filechooser.size_hint = (1, 0.8)
        self.filechooser.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        self.add_widget(self.filechooser)


        button_volver = Button(text="Aceptar y Volver a Inicio",
                               on_press=self.volver_a_inicio,
                               size_hint=(None, None),
                               size=(300, 70),
                               pos_hint={'center_x': 0.80, 'center_y': 0.15})
        button_volver.background_color = (0.2, 0.6, 1, 1)

        button_importar = Button(text="Importar CSV",
                                 on_press=self.importar_csv,
                                 size_hint=(None, None),
                                 size=(300, 70),
                                 pos_hint={'center_x': 0.80, 'center_y': 0.25})
        button_importar.background_color = (0.2, 0.6, 1, 1)

        instruccion = Label(text = "Importar archivos CSV de solo \n  2 Columnas y solo numeros",
                            font_size = '20sp',
                            pos_hint = {'center_x': 0.20, 'center_y': 0.2},
                            color = (1, 1, 1, 1),
                            bold = True
                            )


        self.add_widget(button_importar)
        self.add_widget(instruccion)
        self.add_widget(button_volver)

    def volver_a_inicio(self, instance):
        self.manager.current = 'inicio'

    def importar_csv(self, instance):
        app = App.get_running_app()
        listaX = []
        listaY = []

        selected_file = self.filechooser.selection[0]
        with open(selected_file, 'r') as f:
            reader = csv.reader(f, delimiter=';')  # Asegúrate de usar el delimitador correcto
            for row in reader:
                listaX.append(row[0])  # Agrega el primer elemento de la fila a la columna1
                listaY.append(row[1])  # Agrega el segundo elemento de la fila a la columna2

        app.data_to_pass_CSVlarge = len(listaX)
        app.data_to_pass_CSVX = listaX
        app.data_to_pass_CSVY = listaY

