import flet as ft

class Home(ft.View):
    def __init__(
            self,
            page: ft.Page
    ):
        super().__init__()
        self.page = page
        self.route = '/'
        self.padding = ft.padding.all(0)
        self.controls= [
            
        ]