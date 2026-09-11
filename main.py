import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image

def get_path(filename):
    return os.path.join(os.path.dirname(__file__), filename)

class MainApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        icon_path = get_path('app_icon.png')
        if os.path.exists(icon_path):
            img = Image(source=icon_path, size_hint=(1, 0.4))
            layout.add_widget(img)
            
        title = Label(
            text="Welcome to Ahmed App",
            font_size='24sp',
            bold=True,
            size_hint=(1, 0.2)
        )
        layout.add_widget(title)
        
        btn = Button(
            text="Click Here",
            size_hint=(1, 0.2),
            background_color=(0.2, 0.6, 1, 1)
        )
        layout.add_widget(btn)
        
        return layout

if __name__ == '__main__':
    MainApp().run()
