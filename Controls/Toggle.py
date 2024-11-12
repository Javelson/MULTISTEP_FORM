import flet as ft

class Toggle(ft.Switch):
    def __init__(
            self,
            page: ft.Page
    ):
        super().__init__()
        self.page = page
        self.focus_color = None
        self.hover_color = None
        self.height = 35
        self.top = 10
        self.right = 10
        self.on_change = self.change_theme


    def change_theme( self, e: ft.ControlEvent):
        if self.value == True:
            self.page.theme_mode = ft.ThemeMode.DARK
        else: 
            self.page.theme_mode = ft.ThemeMode.LIGHT

        self.page.update()