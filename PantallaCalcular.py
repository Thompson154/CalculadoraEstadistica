from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button


class PantallaCalcular(Screen):
    def __init__(self, **kwargs):
        super(PantallaCalcular, self).__init__(**kwargs)
        self.add_widget(Button(text="Volver a Inicio", on_press=self.volver_a_inicio))

    def volver_a_inicio(self, instance):
        self.manager.current = 'inicio'