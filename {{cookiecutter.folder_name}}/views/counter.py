import flet as ft
import flet_easy as fs

counter = fs.AddPagesy(
    route_prefix="/counter",
)


# We add a second page
@counter.page(route="/test/{id}", title="Counter")
def counter_page(data: fs.Datasy, id: str):
    page = data.page
    view = data.view

    txt_number = ft.TextField(value=id, text_align="right", width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    return ft.View(
        controls=[
            ft.Text("Counter page", size=30),
            ft.Row(
                [
                    ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                    txt_number,
                    ft.IconButton(ft.icons.ADD, on_click=plus_click),
                ],
                alignment="center",
            ),
        ],
        vertical_alignment="center",
        horizontal_alignment="center",
        appbar=view.appbar,
    )
