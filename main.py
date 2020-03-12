from kivy.app import App
from kivy.uix.label import Label


class NordScrib(App):
    """
    An App that allows you to convert English sentences to Nordic Accent.
    """

    def build(self):
        return Label(text="Hello")


if __name__ == "__main__":
    NordScrib().run()
