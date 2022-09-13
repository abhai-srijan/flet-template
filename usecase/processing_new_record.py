from flet import Page, Container, Text, Row, ElevatedButton, alignment


class ProcessNewRecord:

    def __init__(self, page: Page):
        self.page = page

    def load_layout(self):
        header = Container(
            content=Text("Load New Record"),
            alignment=alignment.center
        )

        nav_ = Container(content=ElevatedButton(text="Back to Home", on_click=lambda _: self.page.go("/")))

        body = Container(content=Text("This is body"),alignment=alignment.center)

        return [header, nav_, body]

