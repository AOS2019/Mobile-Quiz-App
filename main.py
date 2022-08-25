from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager
from kivy.config import Config
from kivy.core.window import  Window


Config.set("kivy", "exit_on_escape", "0")
Window.softinput_mode = 'below_target'
Window.size = (350, 600)



class Quiz(MDApp):
    global screen_manager
    screen_manager = ScreenManager()
    
    
    def build(self):
        self.title = "AOS Quiz App"
        self.icon = "assets/Xsm-logo.png"
        self.theme_cls.primary_palette = "LightBlue"
        screen_manager.add_widget(Builder.load_file("splashScreen.kv"))
        screen_manager.add_widget(Builder.load_file("home.kv"))
        return screen_manager
    
    
    def on_start(self):
        Clock.schedule_once(self.change_screen, 4)
    
    
    def change_screen(self, dt):
        screen_manager.current = "Home"
    
    
Quiz().run()