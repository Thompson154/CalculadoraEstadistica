from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
from kivy.uix.label import Label

class PantallaInicio(Screen):
    def __init__(self, **kwargs):
        super(PantallaInicio, self).__init__(**kwargs)


        background = Image(source='backgroundmejor.jpeg', allow_stretch=True)

        self.add_widget(background)

        title = Label(text="Su Calculadora de\n      Estadística",
                      font_size='40sp',
                      pos_hint={'center_x': 0.5, 'center_y': 0.92},
                      color=(0, 0, 0, 1)
                      )

        susDatos = Label(text="Sus Datos",
                      font_size='20sp',
                      pos_hint={'center_x': 0.32, 'center_y': 0.77},
                      color=(0, 0, 0, 1)
                      )

        self.susDatosListaX = Label(text="Aqui aparecera sus Datos en X",
                         font_size='15sp',
                         pos_hint={'center_x': 0.40, 'center_y': 0.65},
                         color=(0, 0, 0, 1)
                         )

        self.susDatosListaY = Label(text="Aqui aparecera sus Datos en Y",
                              font_size='15sp',
                              pos_hint={'center_x': 0.40, 'center_y': 0.55},
                              color=(0, 0, 0, 1)
                              )



        button_importar_csv = Button(text="Ir a Importar CSV",
                                     on_press=self.ir_a_importar_csv,
                                     size_hint=(None, None),
                                     size=(300, 70),
                                     pos_hint={'center_x': 0.25,'center_y': 0.2})

        button_importar_csv.background_color = (0.2, 0.6, 1, 1)

        button_agregar_manualmente = Button(text="Ir a Agregar Manualmente",
                                            on_press=self.ir_a_agregar_manualmente,
                                            size_hint=(None, None),
                                            size=(300, 70),
                                            pos_hint={'center_x': 0.25,'center_y': 0.1})

        button_agregar_manualmente.background_color = (0.2, 0.6, 1, 1)

        button_calcular = Button(text="Ir a Calcular",
                                 on_press=self.ir_a_calcular,
                                 size_hint=(None, None),
                                 size=(300, 70),
                                 pos_hint={'center_x': 0.80,'center_y': 0.1})

        button_calcular.background_color = (0.2, 0.6, 1, 1)




        self.add_widget(title)
        self.add_widget(susDatos)
        self.add_widget(self.susDatosListaX)
        self.add_widget(self.susDatosListaY)
        self.add_widget(button_importar_csv)
        self.add_widget(button_agregar_manualmente)
        self.add_widget(button_calcular)

    def ir_a_importar_csv(self, instance):
        self.manager.current = 'importar_csv'

    def ir_a_agregar_manualmente(self, instance):
        self.manager.current = 'agregar_manualmente'

    def ir_a_calcular(self, instance):
        self.manager.current = 'calcular'
    def on_enter(self, *args):
        app = App.get_running_app()
        self.susDatosListaX.text = "X: " + ', '.join(app.data_to_pass_X)
        self.susDatosListaY.text = "Y: " + ', '.join(app.data_to_pass_Y)
        self.susDatosListaX.text = "X: " + ', '.join(app.data_to_pass_CSVX)
        self.susDatosListaY.text = "Y: " + ', '.join(app.data_to_pass_CSVY)






