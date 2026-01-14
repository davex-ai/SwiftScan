from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.uix.button import Button

class ScannerApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.cam = Camera(play=True)
        layout.add_widget(self.cam)

        btn = Button(text="Capture")
        btn.bind(on_press=self.capture)
        layout.add_widget(btn)
        return layout

    def capture(self, *args):
        self.cam.export_to_png("document.png")
        print("Saved!")

ScannerApp().run()
