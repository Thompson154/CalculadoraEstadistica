from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.image import Image

class PantallaAgregarManualmente(Screen):
    def __init__(self, **kwargs):
        super(PantallaAgregarManualmente, self).__init__(**kwargs)

        background = Image(source='background_Manual.jpg', allow_stretch=True)
        #hay que poner otra mejor imagen
        self.add_widget(background)

        button_volver = Button(text="Aceptar y Volver a Inicio",
                                     on_press=self.volver_a_inicio,
                                     size_hint=(None, None),
                                     size=(300, 70),
                                     pos_hint={'center_x': 0.80, 'center_y': 0.15})
        button_volver.background_color = (0.2, 0.6, 1, 1)



        textTamnioDeListas = Label(text="Agregue el largo de sus Listas en \n   Ejemplo: 6 ",
                                font_size='20sp',
                                pos_hint={'center_x': 0.25, 'center_y': 0.82},
                                color=(0, 0, 0, 1),
                                bold=True
                                )

        self.inputLargeList = TextInput(
            size_hint=(None, None),
            width=100,
            height=50,
            pos_hint={'center_x': 0.50, 'center_y': 0.82}
        )


        textAgregarList = Label(text="Agregue su Lista en X y Y \n       Ejemplo = 1 2 3 4 5",
                             font_size='20sp',
                             pos_hint={'center_x': 0.20, 'center_y': 0.5},
                             color=(0, 0, 0, 1),
                             bold=True
                             )

        inputListX = TextInput(
            text= "En X",
            size_hint=(None, None),
            width=500,
            height=80,
            pos_hint={'center_x': 0.55, 'center_y': 0.62}
        )

        inputListY = TextInput(
            text="En Y",
            size_hint=(None, None),
            width=500,
            height=80,
            pos_hint={'center_x': 0.55, 'center_y': 0.42}
        )


        self.add_widget(button_volver)
        self.add_widget(textTamnioDeListas)
        self.add_widget(self.inputLargeList)
        self.add_widget(textAgregarList)
        self.add_widget(inputListX)
        self.add_widget(inputListY)

    def volver_a_inicio(self, instance):

        # app = App.get_running_app()
        # app.data_to_pass = self.inputLargeList


        self.manager.current = 'inicio'