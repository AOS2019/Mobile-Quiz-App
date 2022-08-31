from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty
from kivy.config import Config
from kivy.core.window import  Window


from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineIconListItem, MDList


Config.set("kivy", "exit_on_escape", "0")
Window.softinput_mode = 'below_target'
Window.size = (350, 600)


KV = '''
# Menu item in the DrawerList list.
<ItemDrawer>:
    theme_text_color: "Custom"
    on_release: self.parent.set_color_item(self)

    IconLeftWidget:
        id: icon
        icon: root.icon
        theme_text_color: "Custom"
        text_color: root.text_color


<ContentNavigationDrawer>:
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"

    AnchorLayout:
        anchor_x: "left"
        size_hint_y: None
        height: avatar.height

        Image:
            id: avatar
            size_hint: None, None
            size: "56dp", "56dp"
            source: "data/logo/kivy-icon-256.png"

    MDLabel:
        text: "KivyMD library"
        font_style: "Button"
        adaptive_height: True

    MDLabel:
        text: "kivydevelopment@gmail.com"
        font_style: "Caption"
        adaptive_height: True

    ScrollView:

        DrawerList:
            id: md_list



MDScreen:
   
    MDNavigationLayout:

        ScreenManager:

            MDScreen:

                MDBoxLayout:
                    orientation: 'vertical'

                    MDTopAppBar:
                        title: "Navigation Drawer"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]

                    Widget:
                    MDGridLayout:
                        size_hint_y: None
                        height: self.minimum_height
                        width: self.minimum_width
                        cols: 2
                        pos_hint: {'x': 0.0, 'y': 0.09}
                        spacing: "20dp", "50dp"
                        padding: "20dp"

                        RoundedButton:
                            id: btn1
                            text:'Home'
                            icon: "home"
                            orientation: 'vertical'
                            size_hint: 1, None
                            height: "200dp"

                        RoundedButton:
                            id: btn2
                            text:'Join Community'
                            icon: "account-group"
                            orientation: 'vertical'
                            size_hint: 1, None
                            height: "200dp"

                        RoundedButton:
                            id: btn3
                            text:'visit our website'
                            icon: "web"
                            orientation: 'vertical'
                            size_hint: 1, None
                            height: "200dp"
                            on_press: app.our_webpage()

                        RoundedButton:
                            id: btn4
                            text:'contact us'
                            icon: "whatsapp"
                            orientation: 'vertical'
                            size_hint: 1, None
                            height: "200dp"



    MDNavigationDrawer:
        id: nav_drawer

        ContentNavigationDrawer:
            id: content_drawer
            
                

<RoundedButton@Button>
    background_color: (0,0,0,0)
    background_normal: ''
    color: app.theme_cls.accent_color
    icon_size: "50sp"
    canvas.before:
        Color:
            rgba: (70/255, 78/255, 81/255, 0.9)
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: [15]

'''


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


class TestNavigationDrawer(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        icons_item = {
            "folder": "My files",
            "account-multiple": "Shared with me",
            "star": "Starred",
            "history": "Recent",
            "checkbox-marked": "Shared with me",
            "upload": "Upload",
        }
        for icon_name in icons_item.keys():
            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=icons_item[icon_name])
            )


TestNavigationDrawer().run()