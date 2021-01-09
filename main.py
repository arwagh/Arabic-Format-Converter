import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
import bidi.algorithm


#Load the .kv file,
#we don't need to name it like the main class if we do this
#This is the first way of doing it
Builder.load_file('main-design.kv')


class MyGridLayout(Widget):


    def press_img(self):
        pass

    def press_video(self):
        pass

    def press_audio(self):
        pass


class ArabicFormatConvertor(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    ArabicFormatConvertor().run()