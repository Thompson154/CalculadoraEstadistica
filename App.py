from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
import re
number_pattern = re.compile("^[0-9]+$") # lo que tendria que hacer limitar en los text input solo numeros y no letras
# que nos daria un error


class CalculadoraEstadistica(App):
    def build(self):
        sm = ScreenManager()

        inicio_screen = Screen(name='inicio')

        background = Image(source='backgroundmejor.jpeg', allow_stretch=True)

        # Título
        title = Label(text="Su Calculadora de\nEstadística",
                      font_size='40sp',
                      pos_hint={'center_x': 0.5, 'center_y': 0.92},
                      color=(0, 0, 0, 1)
                      )


        listaX = Label(text="LA LISTA DE X APARECERA ACA",
                      font_size='20sp',
                      pos_hint={'center_x': 0.5, 'center_y': 0.7},
                      color=(0, 0, 0, 1)
                       )
        listaY = Label(text="LA LISTA DE Y APARECERA ACA",
                       font_size='20sp',
                       pos_hint={'center_x': 0.5, 'center_y': 0.55},
                       color=(0, 0, 0, 1)
                       )

        # Botones
        buttonCVS = Button(text="Agregar Datos CSV",
                           size_hint=(None, None),
                           size=(300, 100),
                           background_color=(0.2, 0.6, 1, 1),
                           pos_hint={'center_x': 0.16, 'center_y': 0.3}
                           )

        buttonMANUAL = Button(text="Agregar Datos Manualmente",
                              size_hint=(None, None),
                              size=(300, 100),
                              background_color=(0.2, 0.6, 1, 1),
                              pos_hint={'center_x': 0.16, 'center_y': 0.15}
                              )

        buttonCalcular = Button(text="Calcular",
                                size_hint=(None, None),
                                size=(300, 100),
                                background_color=(0.2, 0.6, 1, 1),
                                pos_hint={'center_x': 0.85, 'center_y': 0.15}
                                )

        buttonCVS.bind(on_press=self.pantallaCSV)
        buttonMANUAL.bind(on_press=self.pantallaManual)
        buttonCalcular.bind(on_press=self.pantallaCalcular)

        inicio_screen.add_widget(background)
        inicio_screen.add_widget(listaX)
        inicio_screen.add_widget(listaY)
        inicio_screen.add_widget(title)
        inicio_screen.add_widget(buttonCVS)
        inicio_screen.add_widget(buttonMANUAL)
        inicio_screen.add_widget(buttonCalcular)

        sm.add_widget(inicio_screen)

        return sm

    def pantallaCSV(self, instance):
        sm = self.root

        csv_screen = Screen(name='csv')

        # Aca el código

        buttonAceptar = Button(text="Calcular",
                                size_hint=(None, None),
                                size=(300, 100),
                                background_color=(0.2, 0.6, 1, 1),
                                pos_hint={'center_x': 0.85, 'center_y': 0.15}
                                )

        labelprueba = Label(text="HOla")

        csv_screen.add_widget(labelprueba)
        csv_screen.add_widget(buttonAceptar)

        sm.add_widget(csv_screen)
        sm.current = 'csv'

    def pantallaManual(self, instance):
        sm = self.root

        manual_screen = Screen(name='manual')

        background = Image(source='backgroundmejor.jpeg', allow_stretch=True)


        arregloXN = Label(text="Agregue el largo en X",
                  font_size='20sp',
                  pos_hint={'center_x': 0.15, 'center_y': 0.92},
                  color=(0, 0, 0, 1),
                  bold=True
        )

        arregloYN = Label(text="Agregue el largo en Y",
                          font_size='20sp',
                          pos_hint={'center_x': 0.15, 'center_y': 0.82},
                          color=(0, 0, 0, 1),
                          bold=True
                          )


        longitudXN = TextInput(
            size_hint=(None, None),  # Desactiva el ajuste automático de tamaño
            width=200,  # Establece el ancho
            height=50,  # Establece la altura
            pos_hint={'center_x': 0.40, 'center_y': 0.92}  # Posición centrada
        )

        longitudYN = TextInput(
            size_hint=(None, None),  # Desactiva el ajuste automático de tamaño
            width=200,  # Establece el ancho
            height=50,  # Establece la altura
            pos_hint={'center_x': 0.40, 'center_y': 0.82}  # Posición centrada
        )

        # Aca el código
        buttonAceptar = Button(text="Calcular",
                               size_hint=(None, None),
                               size=(300, 100),
                               background_color=(0.2, 0.6, 1, 1),
                               pos_hint={'center_x': 0.85, 'center_y': 0.15}
                               )

        manual_screen.add_widget(background)
        manual_screen.add_widget(arregloXN)
        manual_screen.add_widget(arregloYN)
        manual_screen.add_widget(longitudXN)
        manual_screen.add_widget(longitudYN)

        manual_screen.add_widget(buttonAceptar)
        sm.add_widget(manual_screen)
        sm.current = 'manual'

    def pantallaCalcular(self, instance):
        sm = self.root

        calcular_screen = Screen(name='calcular')

        background = Image(source='backgroundmejor.jpeg', allow_stretch=True)

        # Aca el código

        botonImportarCSV = Button(text="Importar a CSV",
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
        ingreseX = Label(text="Ingrese un intervalo en x : ",
                         font_size='20sp',
                         pos_hint={'center_x': 0.18, 'center_y': 0.95},
                         color=(0, 0, 0, 1),
                         bold=True
                         )
        inicioX = TextInput(
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
        finalX = TextInput(
            size_hint=(None, None),  # Desactiva el ajuste automático de tamaño
            width=200,  # Establece el ancho
            height=50,  # Establece la altura
            pos_hint={'center_x': 0.62, 'center_y': 0.95}  # Posición centrada
        )
        # Para Y
        ingreseY = Label(text="Ingrese un intervalo en y : ",
                         font_size='20sp',
                         pos_hint={'center_x': 0.18, 'center_y': 0.90},
                         color=(0, 0, 0, 1),
                         bold=True
                         )
        inicioY = TextInput(
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
        finalY = TextInput(size_hint=(None, None),  # Desactiva el ajuste automático de tamaño
            width=200,  # Establece el ancho
            height=50,  # Establece la altura
            pos_hint={'center_x': 0.62, 'center_y': 0.90}  # Posición centrada
        )

        sumaX = Label(text="La Suma de X y Y : ",
                      font_size='20sp',
                      pos_hint={'center_x': 0.15, 'center_y': 0.82},
                      color=(0, 0, 0, 1),
                      bold=True
                      )
        promedioX = Label(text="El Promedio de X y Y : ",
                          font_size='20sp',
                          pos_hint={'center_x': 0.15, 'center_y': 0.62},
                          color=(0, 0, 0, 1),
                          bold=True
                          )
        minimoX = Label(text="El Mínimo de X y Y : ",
                        font_size='20sp',
                        pos_hint={'center_x': 0.15, 'center_y': 0.42},
                        color=(0, 0, 0, 1),
                        bold=True
                        )
        maximoX = Label(text="El Máximo de X y Y : ",
                        font_size='20sp',
                        pos_hint={'center_x': 0.15, 'center_y': 0.22},
                        color=(0, 0, 0, 1),
                        bold=True
                        )

        calcular_screen.add_widget(background)
        calcular_screen.add_widget(inicioX)
        calcular_screen.add_widget(a)
        calcular_screen.add_widget(finalX)
        calcular_screen.add_widget(inicioY)
        calcular_screen.add_widget(a2)
        calcular_screen.add_widget(finalY)
        calcular_screen.add_widget(ingreseX)
        calcular_screen.add_widget(ingreseY)
        calcular_screen.add_widget(sumaX)
        calcular_screen.add_widget(promedioX)
        calcular_screen.add_widget(minimoX)
        calcular_screen.add_widget(maximoX)
        calcular_screen.add_widget(botonImportarCSV)
        calcular_screen.add_widget(botonConsultar)

        sm.add_widget(calcular_screen)
        sm.current = 'calcular'


if __name__ == '__main__':
    CalculadoraEstadistica().run()
