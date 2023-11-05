from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MiApp(App):
    def build(self):
        # Crea un layout BoxLayout vertical
        layout = BoxLayout(orientation='vertical')

        # Crea una lista con 10 números
        numeros = [numero for numero in range(10)]

        # Crea un Label y configúralo con los números
        label = Label(text=f"Numeros: {numeros}",
                      font_size='20sp',
                      pos_hint={'center_x': 0.2, 'center_y': 0.92}
                      )

        # Agrega el Label al layout
        layout.add_widget(label)

        return layout

if __name__ == "__main__":
    MiApp().run()
