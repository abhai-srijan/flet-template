from flet import Page, View

from usecase import LoadMainPage
from usecase.process_existing_record import ProcessExistingRecord
from usecase.processing_new_record import ProcessNewRecord


class Router:
    def __init__(self,page:Page):

        self.page = page

    def route_change(self,e):
        self.page.views.clear()
        self.page.views.append(
            View(
                route="/",
                controls=[LoadMainPage(self.page).load_layout()]
            )
        )

        if self.page.route == "/process_new_record":
            self.page.views.append(
                View(
                    route="/process_new_record",
                    controls=ProcessNewRecord(self.page).load_layout()
                )
            )

        if self.page.route == "/process_existing_record":
            self.page.views.append(
                View(
                    route="/process_existing_record",
                    controls=ProcessExistingRecord(self.page).load_layout()
                )
            )

        self.page.update()
