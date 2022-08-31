from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
from kivy.core.window import  Window
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager
from kivy.properties import StringProperty, ListProperty

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineIconListItem, MDList
from kivymd.theming import ThemeManager, ThemableBehavior

import webbrowser






Config.set("kivy", "exit_on_escape", "0")
Window.softinput_mode = 'below_target'
Window.size = (350, 600)
    
    
    
    

class ContentNavigationDrawer(MDBoxLayout):
    pass


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color
    
        
        
        
class Quiz(MDApp):
    global screen_manager
    screen_manager = ScreenManager()
    
    
    def build(self):
        self.title = "AOS Quiz App"
        self.icon = "assets/Xsm-logo.png"
        theme_cls = ThemeManager()
        self.theme_cls.primary_palette = "LightBlue"
        Window.clearcolor = (1,1,1,1)
        screen_manager.add_widget(Builder.load_file("splashScreen.kv"))
        screen_manager.add_widget(Builder.load_file("home.kv"))
        return screen_manager
    
    
    def on_start(self):
        Clock.schedule_once(self.change_screen, 4)
    
    
    def change_screen(self, dt):
        screen_manager.current = "Home"
    #     icons_item = {
    #     "folder": "My files",
    #     "account-multiple": "Shared with me",
    #     "star": "Starred",
    #     "history": "Recent",
    #     "checkbox-marked": "Shared with me",
    #     "upload": "Upload",
    # }
    #     for icon_name in icons_item.keys():
    #         self.root.ids.content_drawer.ids.md_list.add_widget(
    #             ItemDrawer(icon=icon_name, text=icons_item[icon_name])
    #         )
            
        
    def our_webpage(self):
        webbrowser.open('https://aosinfo4allschool.wordpress.com/')
     
    
    
    
Quiz().run()