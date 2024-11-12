from Views.Home import ft, Home
from Controls.Toggle import Toggle


def main(page: ft.Page):
    page.title = '/'
    page.theme_mode = ft.ThemeMode.LIGHT

    home = Home(page = page)
    toggle = Toggle(page=page)

    page.overlay.append(toggle)
    
    def router(router):
        page.views.clear()

        if page.route == '/':
            page.views.append(home)

        page.update()

    page.on_route_change = router
    page.go(page.route)

if __name__ == '__name__':
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)