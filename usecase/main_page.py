from flet import Container, Text, alignment, colors, Page, Row


class LoadMainPage:
    def __init__(self, page: Page):
        self.page = page

    def load_layout(self):
        load_new_record = Container(
            content=Text("Load new record"),
            margin=10,
            padding=10,
            alignment=alignment.center,
            bgcolor=colors.CYAN_200,
            width=150,
            height=150,
            border_radius=10,
            ink=True,
            on_click=lambda _: self.page.go("/process_new_record"),
        )

        load_existing_record = Container(
            content=Text("Load existing record"),
            margin=10,
            padding=10,
            alignment=alignment.center,
            bgcolor=colors.CYAN_200,
            width=150,
            height=150,
            border_radius=10,
            ink=True,
            on_click=lambda e: self.page.go("/process_existing_record"),
        )
        return Row(
            [load_new_record, load_existing_record],
            alignment="center",
        )
