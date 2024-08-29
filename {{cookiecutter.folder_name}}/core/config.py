import flet as ft
import flet_easy as fs


class ConfigApp:
    def __init__(self, app: fs.FletEasy):
        self.app = app
        self.start()

    def start(self):
        @self.app.view
        def view_config(data: fs.Datasy):
            """Adding an AppBar on all pages"""
            return fs.Viewsy(
                appbar=ft.AppBar(
                    title=ft.Text("Flet-Easy"),
                    actions=[
                        ft.FilledButton(
                            text="Home",
                            on_click=data.go(data.route_init),
                        ),
                        ft.VerticalDivider(opacity=0),
                        ft.FilledButton(
                            text="Counter",
                            on_click=data.go("/counter/test/0"),
                        ),
                    ],
                    bgcolor="#121113",
                )
            )

        @self.app.config
        def page_config(page: ft.Page):
            """Removing animation on route change."""
            theme = ft.Theme()
            platforms = ["android", "ios", "macos", "linux", "windows"]
            for platform in platforms:
                setattr(theme.page_transitions, platform, ft.PageTransitionTheme.NONE)
            page.theme = theme
