import flet
from flet import Page

from entrypoint.routes import Router


def main(page: Page):
    page.title = "POC"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    def view_pop(e):
        print("View pop:", e.view)
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = Router(page).route_change
    page.on_view_pop = view_pop
    page.go(page.route)


flet.app(target=main, upload_dir="assest")
