import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
import bidi.algorithm
from kivy.core.window import Window
from img import ImgLayout
from kivy.uix.screenmanager import ScreenManager, Screen


#Define out different screens
class MainWindow(Screen):
    pass

class ImagesWindow(Screen):
    pass

class AudiosWindow(Screen):
    pass

class VideosWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

#Load the .kv file,
#we don't need to name it like the main class if we do this
#This is the first way of doing it
kv = Builder.load_file('main-design.kv')

Window.clearcolor = (1, 1, 1, 1)



class MyLayout(Widget):
    pass

class ArabicFormatConvertor(App):
    def build(self):
        return kv

        
if __name__ == '__main__':
    ArabicFormatConvertor().run()