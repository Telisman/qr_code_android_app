import kivy
import qrcode
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.image import Image

Builder.load_file("test.kv")


class QR_code_Grid(Widget):

    name = ObjectProperty(None)
    url = ObjectProperty(None)


    def press(self):
        name = self.name
        url = self.url
        qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
        )
        qr.add_data(url)
        img = qr.make_image()
        img.save(str(name.text) + ".jpg")
        # print(type(img))
        qr_img= Image(source= img.show())






        self.name.text = ""
        self.url.text = ""


class QR_code_app(App):
    title = "QR code generator"
    def build(self):
        Window.clearcolor = (1, 0, 0, 1)
        return QR_code_Grid()

if __name__ == "__main__":
    QR_code_app().run()
