import flet as ft

class Home(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.container_form = ContainerForm(page=page)
        self.route = '/'
        self.padding = ft.padding.all(0)
        self.controls = [
            ft.ResponsiveRow(
                controls=[
                    self.container_form,
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ]
        self.vertical_alignment = ft.MainAxisAlignment.CENTER

class ContainerForm(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.col = {'xs': 11, 'sm': 4, 'md': 2.90}
        self.bgcolor = ft.colors.with_opacity(0.25, '#84D55A')
        self.border_radius = 3
        self.padding = ft.padding.all(8)
        self.content = ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        PositionForm(page=page, index=1),
                        PositionForm(page=page, index=2),
                        PositionForm(page=page, index=3)
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                ft.Column(
                    controls=[
                        ft.Text(
                            value='Informação pessoal',
                            weight='bold',
                            size=16
                        ),
                        ft.Column(
                            controls=[
                                TextField(hint_text='Primeiro nome'),
                                TextField(hint_text='Último nome')
                            ],
                            spacing=4
                        ),
                        ft.Column(
                            controls=[
                                ft.ResponsiveRow(
                                    controls=[
                                        Button(
                                            text='Voltar',
                                            bgcolor=ft.colors.with_opacity(0.8, 'grey'),
                                            visible = False
                                        )
                                    ]
                                ),
                                 ft.ResponsiveRow(
                                    controls=[
                                        Button(
                                            text='Sequinte',
                                            bgcolor=ft.colors.with_opacity(0.8, 'green')
                                        )
                                    ]
                                )
                            ],
                            spacing=3
                        ),
                    ],
                    spacing=10
                )
            ],
            spacing=25
        )

class PositionForm(ft.Container):
    def __init__(self, page: ft.Page, index: int = 1):
        super().__init__()
        self.page = page
        self.width = 30
        self.height = 30
        self.border_radius = 30
        self.bgcolor = ft.colors.with_opacity(0.60, 'grey')
        self.content = ft.Text(
            value=index,
            size=13,
            weight='bold'
        )
        self.alignment = ft.alignment.center

class TextField(ft.TextField):
    def __init__(self, hint_text: str, autofocus: bool = True, password: bool = False):
        super().__init__()
        self.border_width = 1
        self.border_radius = 3
        self.height = 45
        self.focused_bgcolor = ft.colors.with_opacity(0.05, '#000000')
        self.focused_border_color = ft.colors.GREEN
        self.hint_text = hint_text
        self.hint_style = ft.TextStyle(size=13)
        self.text_style = ft.TextStyle(size=13)
        self.autofocus = autofocus
        self.password = password

class Button(ft.Container):
    def __init__(self, text: str, bgcolor: str, visible: bool= True):
        super().__init__()
        self.bgcolor = bgcolor
        self.original_bgcolor = bgcolor
        self.height = 40
        self.border_radius = 3
        self.alignment = ft.alignment.center
        self.content = ft.Text(
            value=text,
            color=ft.colors.WHITE,
            size=13,
            weight='bold'
        )
        self.visible = visible
        self.on_hover = self.hover

    def hover(self, e: ft.HoverEvent):
        if e.data == 'true':
            e.control.bgcolor = ft.colors.with_opacity(0.80, self.original_bgcolor)
        else:
            e.control.bgcolor = self.original_bgcolor
        e.page.update()
