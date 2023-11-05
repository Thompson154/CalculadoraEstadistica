from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from PantallaAgregarManualmente import PantallaAgregarManualmente
from PantallaCalcular import PantallaCalcular
from PantallaImportarCSV import PantallaImportarCSV
from PantallaInicio import PantallaInicio


class CalculadoraEstadisticaApp(App):
    data_to_pass_X = ""
    data_to_pass_Y = ""
    def build(self):
        sm = ScreenManager()
        sm.add_widget(PantallaInicio(name='inicio'))
        sm.add_widget(PantallaImportarCSV(name='importar_csv'))
        sm.add_widget(PantallaAgregarManualmente(name='agregar_manualmente'))
        sm.add_widget(PantallaCalcular(name='calcular'))
        return sm

    def on_stop(self):
        CalculadoraEstadisticaApp.data_to_pass_X = ""
        CalculadoraEstadisticaApp.data_to_pass_Y = ""


if __name__ == '__main__':
    CalculadoraEstadisticaApp().run()