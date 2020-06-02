import func
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.config import Config

SENDER_EMAIL = "Почта отправителя"
SENDER_NAME = "Имя отправителя"
RECEPIENT_NAME = "Уважаемый абонент"
SENDER_PASSWORD='Пароль отправителя'
PROVIDER_NAME = "Наименование провайдера"

Config.set("graphics", "resizable", "0")
Config.set("graphics", "width", "300")
Config.set("graphics", "height", "420")

class ManualerApp(App):
    def send_mail(self, text):
        func.make_doc(self.abon_login.text, self.abon_password.text)
        func.mail_sender(self.sender_name.text, self.sender_password.text, self.sender_mail.text, self.abon_mail.text, self.abon_name.text, PROVIDER_NAME)

    def build(self):
        root = BoxLayout(orientation='vertical')
        self.abon_name = TextInput(text = RECEPIENT_NAME, readonly = False, font_size = 20, size_hint = [1,.1], background_color = [1,1,1,.8])
        self.abon_mail = TextInput(text="", readonly=False, font_size=20, size_hint=[1, .1], background_color=[1, 1, 1, .8])
        self.abon_login = TextInput(text="", readonly=False, font_size=20, size_hint=[1, .1], background_color=[1, 1, 1, .8])
        self.abon_password = TextInput(text="", readonly=False, font_size=20, size_hint=[1, .1], background_color=[1, 1, 1, .8])
        self.sender_name = TextInput(text=SENDER_NAME, readonly=False, font_size=20, size_hint=[1, .1], background_color=[.3, 1, .7, .8])
        self.sender_mail = TextInput(text=SENDER_EMAIL, readonly=False, font_size=20, size_hint=[1, .1], background_color=[.3, 1, .7, .8])
        self.sender_password = TextInput(text=SENDER_PASSWORD, readonly=False, font_size=20, size_hint=[1, .1], background_color=[.3, 1, .7, .8])

        root.add_widget(Label(text="Абонент ", size_hint=[1,.2]))

        abon = GridLayout(cols=2)
        abon.add_widget(Label(text="Имя: ", size_hint=[.4,.1]))
        abon.add_widget(self.abon_name)
        abon.add_widget(Label(text="Почта: ", size_hint=[.4, .1]))
        abon.add_widget(self.abon_mail)
        abon.add_widget(Label(text="Логин: ", size_hint=[.4, .1]))
        abon.add_widget(self.abon_login)
        abon.add_widget(Label(text="Пароль: ", size_hint=[.4, .1]))
        abon.add_widget(self.abon_password)
        root.add_widget(abon)

        root.add_widget(Label(text="Отправитель ", size_hint=[1, .2]))

        sender = GridLayout(cols=2, size_hint=[1,.7])
        sender.add_widget(Label(text="Имя: ", size_hint=[.4, .1]))
        sender.add_widget(self.sender_name)
        sender.add_widget(Label(text="Почта: ", size_hint=[.4, .1]))
        sender.add_widget(self.sender_mail)
        sender.add_widget(Label(text="Пароль: ", size_hint=[.4, .1]))
        sender.add_widget(self.sender_password)
        root.add_widget(sender)

        btn1=Button(text = 'Отправить', size_hint=[1, .25], on_press=self.send_mail)
        root.add_widget(btn1)

        return root

if __name__ == "__main__":
    ManualerApp().run()









