import csv

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.image import Image
from matplotlib import pyplot as plt

import segmentTree

class PantallaCalcular(Screen):
    def __init__(self, **kwargs):
        super(PantallaCalcular, self).__init__(**kwargs)

        background = Image(source='background_Manual2.jpg', allow_stretch=True)

        self.add_widget(background)

        # Aca el código

        button_volver = Button(text="Volver a Inicio",
                               on_press=self.volver_a_inicio,
                               size_hint=(None, None),
                               size=(300, 70),
                               pos_hint={'center_x': 0.85, 'center_y': 0.2})
        button_volver.background_color = (0.2, 0.6, 1, 1)


        self.botonImportarCSV = Button(text="Exportar a CSV",
                                  size_hint=(None, None),
                                  on_press=self.exportar_csv,
                                  size=(300, 100),
                                  background_color=(0.2, 0.6, 1, 1),
                                  pos_hint={'center_x': 0.85, 'center_y': 0.1}
                                  )

        botonConsultarManual = Button(text="Consultar si Agrego \n Datos Manualmente",
                                size_hint=(None, None),
                                size=(300, 100),
                                on_press=self.calcularConSegmentTreeManual,
                                background_color=(0.2, 0.6, 1, 1),
                                pos_hint={'center_x': 0.85, 'center_y': 0.925}
                                )

        botonConsultarCSV = Button(text="Consultar si Agrego \n Datos importando CSV",
                                size_hint=(None, None),
                                size=(300, 100),
                                on_press=self.calcularConSegmentTreeCSV,
                                background_color=(0.2, 0.6, 1, 1),
                                pos_hint={'center_x': 0.85, 'center_y': 0.8}
                                )

        # Para X
        ingreseX = Label(text="Ingrese un intervalo de: ",
                         font_size='20sp',
                         pos_hint={'center_x': 0.18, 'center_y': 0.9},
                         color=(0, 0, 0, 1),
                         bold=True
                         )
        self.inicioX = TextInput(
            size_hint=(None, None),  # Desactiva el ajuste automático de tamaño
            width=200,  # Establece el ancho
            height=50,  # Establece la altura
            pos_hint={'center_x': 0.42, 'center_y': 0.9}  # Posición centrada
        )
        a = Label(text="a",
                  font_size='20sp',
                  pos_hint={'center_x': 0.52, 'center_y': 0.9},
                  color=(0, 0, 0, 1),
                  bold=True
                  )
        self.finalX = TextInput(
            size_hint=(None, None),  # Desactiva el ajuste automático de tamaño
            width=200,  # Establece el ancho
            height=50,  # Establece la altura
            pos_hint={'center_x': 0.62, 'center_y': 0.9}  # Posición centrada
        )
        # Para Y
        # ingreseY = Label(text="Ingrese un intervalo en Y: ",
        #                  font_size='20sp',
        #                  pos_hint={'center_x': 0.18, 'center_y': 0.90},
        #                  color=(0, 0, 0, 1),
        #                  bold=True
        #                  )
        # self.inicioY = TextInput(
        #     size_hint=(None, None),  # Desactiva el ajuste automático de tamaño
        #     width=200,  # Establece el ancho
        #     height=50,  # Establece la altura
        #     pos_hint={'center_x': 0.42, 'center_y': 0.90}  # Posición centrada
        # )
        # a2 = Label(text="a",
        #            font_size='20sp',
        #            pos_hint={'center_x': 0.52, 'center_y': 0.90},
        #            color=(0, 0, 0, 1),
        #            bold=True
        #            )
        # self.finalY = TextInput(size_hint=(None, None),  # Desactiva el ajuste automático de tamaño
        #                    width=200,  # Establece el ancho
        #                    height=50,  # Establece la altura
        #                    pos_hint={'center_x': 0.62, 'center_y': 0.90}  # Posición centrada
        #                    )

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

        self.mostrarSuma = Label(text=" Resultado ",
                            font_size='20sp',
                            pos_hint={'center_x': 0.35, 'center_y': 0.82},
                            color=(0, 0, 0, 1),
                            bold=True
                            )

        self.mostrarPromedio = Label(text="Resultado",
                                font_size='20sp',
                                pos_hint={'center_x': 0.35, 'center_y': 0.62},
                                color=(0, 0, 0, 1),
                                bold=True
                                )

        self.mostrarMinimo = Label(text="Resultado",
                              font_size='20sp',
                              pos_hint={'center_x': 0.35, 'center_y': 0.42},
                              color=(0, 0, 0, 1),
                              bold=True
                              )
        self.mostrarMaximo= Label(text="Resultado",
                            font_size='20sp',
                            pos_hint={'center_x': 0.35, 'center_y': 0.22},
                            color=(0, 0, 0, 1),
                            bold=True
                            )



        self.add_widget(self.botonImportarCSV)
        self.add_widget(button_volver)
        self.add_widget(botonConsultarManual)
        self.add_widget(botonConsultarCSV)
        self.add_widget(ingreseX)
        self.add_widget(self.inicioX)
        self.add_widget(a)
        self.add_widget(self.finalX)
        #self.add_widget(ingreseY)
        #self.add_widget(self.inicioY)
        #self.add_widget(a2)
        #self.add_widget(self.finalY)
        self.add_widget(suma)
        self.add_widget(self.mostrarSuma)
        self.add_widget(promedio)
        self.add_widget(self.mostrarPromedio)
        self.add_widget(maximo)
        self.add_widget(self.mostrarMaximo)
        self.add_widget(minimo)
        self.add_widget(self.mostrarMinimo)


    def volver_a_inicio(self, instance):
        self.manager.current = 'inicio'


    def calcularConSegmentTreeManual(self,*args):
        app = App.get_running_app()
        n = int(app.data_to_pass_tamanioListas)
        listaX = list(map(int, app.data_to_pass_X))  # Convertir los elementos de la lista en enteros
        listaY = list(map(int, app.data_to_pass_Y))  # Convertir los elementos de la lista en enteros
        segmentTree.a = listaX
        segmentTree.init(0, n - 1, 0)
        resultadoX = segmentTree.query(0, n - 1, 0, int(self.inicioX.text), int(self.finalX.text))
        segmentTree.a = listaY
        segmentTree.init(0, n - 1, 0)
        resultadoY = segmentTree.query(0, n - 1, 0, int(self.inicioX.text), int(self.finalX.text))
        self.mostrarMaximo.text = str(resultadoX.max) + " " + str(resultadoY.max)
        self.mostrarMinimo.text = str(resultadoX.min) + " " + str(resultadoY.min)
        self.mostrarPromedio.text = str(resultadoX.promedio) + " " + str(resultadoY.promedio)
        self.mostrarSuma.text = str(resultadoX.sum) + " " + str(resultadoY.sum)


    def calcularConSegmentTreeCSV(self,*args):
        app = App.get_running_app()
        n = int(app.data_to_pass_CSVlarge)
        listaX = list(map(int, app.data_to_pass_CSVX))  # Convertir los elementos de la lista en enteros
        listaY = list(map(int, app.data_to_pass_CSVY))  # Convertir los elementos de la lista en enteros
        segmentTree.a = listaX
        segmentTree.init(0, n - 1, 0)
        resultadoX = segmentTree.query(0, n - 1, 0, int(self.inicioX.text), int(self.finalX.text))
        segmentTree.a = listaY
        segmentTree.init(0, n - 1, 0)
        resultadoY = segmentTree.query(0, n - 1, 0, int(self.inicioX.text), int(self.finalX.text))
        self.mostrarMaximo.text = str(resultadoX.max) + " " + str(resultadoY.max)
        self.mostrarMinimo.text = str(resultadoX.min) + " " + str(resultadoY.min)
        self.mostrarPromedio.text = str(resultadoX.promedio) + " " + str(resultadoY.promedio)
        self.mostrarSuma.text = str(resultadoX.sum) + " " + str(resultadoY.sum)

        # plt.plot(list(map(int, app.data_to_pass_CSVX)), list(map(int, app.data_to_pass_Y)), label='Datos')
        # # Luego, graficamos los puntos de interés:
        # plt.plot(resultadoX.max, 'ro', label='Máximo')
        # plt.plot(resultadoX.min, 'bo', label='Mínimo')
        # plt.plot(resultadoX.gcd, 'go', label='Promedio')
        # plt.plot(resultadoX.sum, 'yo', label='Suma')
        #
        # # Finalmente, mostramos la leyenda y el gráfico:
        # plt.legend()
        # plt.show()

    def exportar_csv(self, instance):
        # Los datos que quieres exportar
        data = [
            ['Intervalo', 'Suma', 'Promedio', 'Mínimo', 'Máximo'],
            [f'{self.inicioX.text}-{self.finalX.text}', self.mostrarSuma.text, self.mostrarPromedio.text,
             self.mostrarMinimo.text, self.mostrarMaximo.text]
        ]
        with open('output.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(data)






