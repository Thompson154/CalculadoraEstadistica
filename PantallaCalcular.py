from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.image import Image

class PantallaCalcular(Screen):
    def __init__(self, **kwargs):
        super(PantallaCalcular, self).__init__(**kwargs)

        background = Image(source='background_Manual.jpg', allow_stretch=True)

        self.add_widget(background)

        # Aca el código

        button_volver = Button(text="Volver a Inicio",
                               on_press=self.volver_a_inicio,
                               size_hint=(None, None),
                               size=(300, 70),
                               pos_hint={'center_x': 0.85, 'center_y': 0.2})
        button_volver.background_color = (0.2, 0.6, 1, 1)


        botonImportarCSV = Button(text="Exportar a CSV",
                                  size_hint=(None, None),
                                  size=(300, 100),
                                  background_color=(0.2, 0.6, 1, 1),
                                  pos_hint={'center_x': 0.85, 'center_y': 0.1}
                                  )

        botonConsultar = Button(text="Consultar",
                                size_hint=(None, None),
                                size=(300, 100),

                                background_color=(0.2, 0.6, 1, 1),
                                pos_hint={'center_x': 0.85, 'center_y': 0.925}
                                )

        # Para X
        ingreseX = Label(text="Ingrese un intervalo en X: ",
                         font_size='20sp',
                         pos_hint={'center_x': 0.18, 'center_y': 0.95},
                         color=(0, 0, 0, 1),
                         bold=True
                         )
        self.inicioX = TextInput(
            size_hint=(None, None),  # Desactiva el ajuste automático de tamaño
            width=200,  # Establece el ancho
            height=50,  # Establece la altura
            pos_hint={'center_x': 0.42, 'center_y': 0.95}  # Posición centrada
        )
        a = Label(text="a",
                  font_size='20sp',
                  pos_hint={'center_x': 0.52, 'center_y': 0.95},
                  color=(0, 0, 0, 1),
                  bold=True
                  )
        self.finalX = TextInput(
            size_hint=(None, None),  # Desactiva el ajuste automático de tamaño
            width=200,  # Establece el ancho
            height=50,  # Establece la altura
            pos_hint={'center_x': 0.62, 'center_y': 0.95}  # Posición centrada
        )
        # Para Y
        ingreseY = Label(text="Ingrese un intervalo en Y: ",
                         font_size='20sp',
                         pos_hint={'center_x': 0.18, 'center_y': 0.90},
                         color=(0, 0, 0, 1),
                         bold=True
                         )
        self.inicioY = TextInput(
            size_hint=(None, None),  # Desactiva el ajuste automático de tamaño
            width=200,  # Establece el ancho
            height=50,  # Establece la altura
            pos_hint={'center_x': 0.42, 'center_y': 0.90}  # Posición centrada
        )
        a2 = Label(text="a",
                   font_size='20sp',
                   pos_hint={'center_x': 0.52, 'center_y': 0.90},
                   color=(0, 0, 0, 1),
                   bold=True
                   )
        self.finalY = TextInput(size_hint=(None, None),  # Desactiva el ajuste automático de tamaño
                           width=200,  # Establece el ancho
                           height=50,  # Establece la altura
                           pos_hint={'center_x': 0.62, 'center_y': 0.90}  # Posición centrada
                           )

        suma = Label(text="La Suma de X y Y : ",
                      font_size='20sp',
                      pos_hint={'center_x': 0.15, 'center_y': 0.82},
                      color=(0, 0, 0, 1),
                      bold=True
                      )

        promedio = Label(text="El Promedio de X y Y : ",
                          font_size='20sp',
                          pos_hint={'center_x': 0.15, 'center_y': 0.62},
                          color=(0, 0, 0, 1),
                          bold=True
                          )


        minimo = Label(text="El Mínimo de X y Y : ",
                        font_size='20sp',
                        pos_hint={'center_x': 0.15, 'center_y': 0.42},
                        color=(0, 0, 0, 1),
                        bold=True
                        )

        maximo = Label(text="El Máximo de X y Y  ",
                        font_size='20sp',
                        pos_hint={'center_x': 0.15, 'center_y': 0.22},
                        color=(0, 0, 0, 1),
                        bold=True
                        )

        mostrarSuma = Label(text=" Resultado ",
                            font_size='20sp',
                            pos_hint={'center_x': 0.35, 'center_y': 0.82},
                            color=(0, 0, 0, 1),
                            bold=True
                            )

        mostrarPromedio = Label(text="Resultado",
                                font_size='20sp',
                                pos_hint={'center_x': 0.35, 'center_y': 0.62},
                                color=(0, 0, 0, 1),
                                bold=True
                                )

        mostrarMinimo = Label(text="Resultado",
                              font_size='20sp',
                              pos_hint={'center_x': 0.35, 'center_y': 0.42},
                              color=(0, 0, 0, 1),
                              bold=True
                              )
        mostrarMaximo= Label(text="Resultado",
                            font_size='20sp',
                            pos_hint={'center_x': 0.35, 'center_y': 0.22},
                            color=(0, 0, 0, 1),
                            bold=True
                            )









        self.add_widget(botonImportarCSV)
        self.add_widget(button_volver)
        self.add_widget(botonConsultar)
        self.add_widget(ingreseX)
        self.add_widget(self.inicioX)
        self.add_widget(a)
        self.add_widget(self.finalX)
        self.add_widget(ingreseY)
        self.add_widget(self.inicioY)
        self.add_widget(a2)
        self.add_widget(self.finalY)
        self.add_widget(suma)
        self.add_widget(mostrarSuma)
        self.add_widget(promedio)
        self.add_widget(mostrarPromedio)
        self.add_widget(maximo)
        self.add_widget(mostrarMaximo)
        self.add_widget(minimo)
        self.add_widget(mostrarMinimo)


    def volver_a_inicio(self, instance):
        self.manager.current = 'inicio'


