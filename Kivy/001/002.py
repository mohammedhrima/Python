from cgitb import text
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1
        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="First Name: "))
        self.fname = TextInput(multiline=False)
        self.inside.add_widget(self.fname)

        self.inside.add_widget(Label(text="Last Name: "))
        self.lname = TextInput(multiline=False)
        self.inside.add_widget(self.lname)

        self.inside.add_widget(Label(text="Age: "))
        self.age = TextInput(multiline=False)
        self.inside.add_widget(self.age)

        self.add_widget(self.inside)
        self.submit = Button(text="Clique me", font_size=20)
        self.add_widget(self.submit)


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__:
    MyApp().run()
