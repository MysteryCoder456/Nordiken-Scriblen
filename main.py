from random import randint
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MainGrid(GridLayout):
    """
    The Main Grid for the UI Elements. Meant to the return in App.build().

    Arguments:
        GridLayout {any} -- Honestly idk
    """

    def __init__(self, **kwargs):
        super(MainGrid, self).__init__(**kwargs)
        self.rows = 3

        self.middle_grid = GridLayout()
        self.middle_grid.cols = 2

        self.title = Label(
            text="Welcome to Nordiken Scriblen!\n" +
            "An App that allows you to convert English sentences to Nordic Accent English.\n" +
            "The results are random and may differ slightly, so try to convert\n" +
            "the same texts multiple times.\n\n" +
            "Enter normal English on the left and the Nordic English will appear so the right.\n" +
            "Have Fun!",
            font_size=40,
            halign="center"
        )
        self.add_widget(self.title)

        self.eng_input = TextInput(
            text="Markiplier is the best YouTuber!. I looooove to watch his videos!",
            font_size=38
        )
        self.middle_grid.add_widget(self.eng_input)

        self.nord_output = TextInput(font_size=38)
        self.middle_grid.add_widget(self.nord_output)
        self.add_widget(self.middle_grid)

        self.convert_btn = Button(
            text="NØRDÎFŸ!",
            font_size=100
        )
        self.convert_btn.bind(on_press=self.convert)
        self.add_widget(self.convert_btn)

    def convert(self, instance):
        text = self.eng_input.text
        words = text.split(" ")
        vowels = "aeiou"
        sen = ""

        for word in words:
            for letter in word:
                vowel = vowels[randint(0, 4)]
                capital = False
                chance = 50

                if letter.isupper():
                    capital = True
                    letter = letter.lower()

                if randint(0, 100) < chance and letter in vowels:
                    if capital:
                        sen += vowel.upper()
                    elif letter == "y" and randint(0, 20) < 12:
                        if capital:
                            sen += "Ee"
                        else:
                            sen += "ee"
                    elif letter == "u" and randint(0, 20) < 12:
                        if capital:
                            sen += "Oo"
                        else:
                            sen += "oo"
                    else:
                        if capital:
                            sen += vowel.upper()
                        else:
                            sen += vowel

                elif letter == "s":
                    if capital:
                        sen += "Zz"
                    else:
                        sen += "zz"
                else:
                    if capital:
                        sen += letter.upper()
                    else:
                        sen += letter

            sen += " "

        self.nord_output.text = sen


class NordScrib(App):
    """
    An App that allows you to convert English sentences to Nordic Accent.
    """

    def build(self):
        return MainGrid()


if __name__ == "__main__":
    NordScrib().run()
