from kivy.core.text import LabelBase
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.core.window import Window

Window.size = (350, 600)


kv = """
MDFloatLayout:
    Card:
        md_bg_color: 1, 1, 1, 1
        elevation: 5
        size_hint: .85, .9
        pos_hint: {"center_x": .5, "center_y": .5}
        radius: [10]
        Image:
            source: "assets//logo1.jpg"
            size_hint: 1, 1
            pos_hint: {"center_x": .5, "center_y": .78}
        MDFloatLayout:
            size_hint: .85, .08
            pos_hint: {"center_x": .5, "center_y": .52}
            canvas:
                Color:
                    rgb: (238/255, 238/255, 238/255, 1)
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [22]
            TextInput:
                hint_text: "Email"
                size_hint: 1, None
                pos_hint: {"center_x": .5, "center_y": .5}
                height: self.minimum_height
                multiline: False
                cursor_color: 57/255, 66/255, 143/255, 1
                cursor_width: "2sp"
                foreground_color: 57/255, 66/255, 143/255, 1
                background_color: 0, 0, 0, 0
                padding: 15
                font_name: "Poppins"
                font_size: "18sp"
        MDFloatLayout:
            size_hint: .85, .08
            pos_hint: {"center_x": .5, "center_y": .41}
            canvas:
                Color:
                    rgb: (238/255, 238/255, 238/255, 1)
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [22]
            TextInput:
                hint_text: "Password"
                size_hint: 1, None
                pos_hint: {"center_x": .5, "center_y": .5}
                height: self.minimum_height
                multiline: False
                password: True
                cursor_color: 57/255, 66/255, 143/255, 1
                cursor_width: "2sp"
                foreground_color: 57/255, 66/255, 143/255, 1
                background_color: 0, 0, 0, 0
                padding: 15
                font_name: "Poppins"
                font_size: "18sp"
        Button:
            text: "LOGIN"
            font_name: "BPoppins"
            font_size: "18sp"
            size_hint: .4, .08
            pos_hint: {"center_x": .29, "center_y": .3}
            background_color: 0, 0, 0, 0
            color: 1, 1, 1, 1
            canvas.before:
                Color:
                    rgb: 11/255, 205/255, 215/255
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [22]
        Button:
            text: "SIGNUP"
            font_name: "BPoppins"
            font_size: "18sp"
            size_hint: .4, .08
            pos_hint: {"center_x": .72, "center_y": .3}
            background_color: 0, 0, 0, 0
            color: 1, 1, 1, 1
            canvas.before:
                Color:
                    rgb: 11/255, 205/255, 215/255
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [22]
        MDLabel:
            text: "OR"
            pos_hint: {"center_x": .5, "center_y": .2}
            font_name: "Poppins"
            font_size: "16sp"
            halign: "center"
        MDFloatLayout:
            md_bg_color: 238/255, 238/255, 238/255, 1
            size_hint: .68, .08
            pos_hint: {"center_x": .5, "center_y": .1}
            radius: [23]
            MDIconButton:
                icon: "google"
                user_font_size: "20sp"
                pos_hint: {"center_x": .1, "center_y": .5}
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1
            MDLabel:
                text: "Sign in with Google"
                pos_hint: {"center_x": .7, "center_y": .5}
                font_name: "Poppins"
"""


class Card(FakeRectangularElevationBehavior, MDFloatLayout):
    pass


class LoginPage(MDApp):
    def build(self):
        return Builder.load_string(kv)


if __name__ == "__main__":
    LabelBase.register(name="Poppins", fn_regular="Your Font Path\\Poppins-Regular.ttf")
    LabelBase.register(name="BPoppins", fn_regular="Your Font Path \\Poppins-SemiBold.ttf")
    LoginPage().run()
