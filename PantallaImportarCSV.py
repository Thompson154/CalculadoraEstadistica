from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.image import Image

class PantallaImportarCSV(Screen):
    def __init__(self, **kwargs):
        super(PantallaImportarCSV, self).__init__(**kwargs)

        background = Image(source='background_Manual.jpg', allow_stretch=True)

        self.add_widget(background)


        button_volver = Button(text="Aceptar y Volver a Inicio",
                               on_press=self.volver_a_inicio,
                               size_hint=(None, None),
                               size=(300, 70),
                               pos_hint={'center_x': 0.80, 'center_y': 0.15})
        button_volver.background_color = (0.2, 0.6, 1, 1)




        self.add_widget(button_volver)

    def volver_a_inicio(self, instance):
        self.manager.current = 'inicio'