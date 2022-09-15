from typing import Dict

from flet import (
    Page,
    Container,
    Text,
    Row,
    ElevatedButton,
    alignment,
    file_picker,
    FilePickerUploadFile,
    FilePicker,
    FilePickerResultEvent,
    icons,
    Ref,
    Column,
    FilePickerUploadEvent,
    ProgressRing,
)


class ProcessNewRecord:
    def __init__(self, page: Page):
        self.page = page
        self.file_picker = FilePicker(
            on_result=self.file_picker_result, on_upload=self.on_upload_progress
        )
        self.prog_bars: Dict[str, ProgressRing] = {}
        self.files = Ref[Column]()
        self.upload_button = Ref[ElevatedButton]()

    def on_upload_progress(self, e: FilePickerUploadEvent):
        self.prog_bars[e.file_name].value = e.progress
        self.prog_bars[e.file_name].update()

    def upload_files(self, e):
        upload_list = []
        print("uploading")
        if self.file_picker.result != None and self.file_picker.result.files != None:
            for f in self.file_picker.result.files:
                upload_list.append(
                    FilePickerUploadFile(
                        f.name,
                        upload_url=self.page.get_upload_url(f.name, 600),
                    )
                )
            self.file_picker.upload(upload_list)

    def file_picker_result(self, e: FilePickerResultEvent):
        self.upload_button.current.disabled = True if e.files == None else False
        self.prog_bars.clear()
        self.files.current.controls.clear()
        if e.files != None:
            for f in e.files:
                prog = ProgressRing(value=0, bgcolor="#eeeeee", width=20, height=20)
                self.prog_bars[f.name] = prog
                self.files.current.controls.append(Row([prog, Text(f.name)]))
        self.page.update()

    def load_layout(self):

        self.page.overlay.append(self.file_picker)
        self.page.update()

        header = Container(
            content=Text("Load New Record"),
            alignment=alignment.center,
            on_click=lambda _: self.file_picker.pick_files(),
        )

        nav_ = Container(
            content=ElevatedButton(
                text="Back to Home", on_click=lambda _: self.page.go("/")
            )
        )
        select_file = Column(
            [
                Container(
                    ElevatedButton(
                        "Choose files...",
                        on_click=lambda _: self.file_picker.pick_files(),
                        icon=icons.FOLDER_OPEN,
                    ),
                    alignment=alignment.center,
                ),
                Container(
                Column(ref=self.files, alignment="center"),alignment=alignment.center
                )
            ],
            alignment="center",
        )

        body = Container(
            ref=self.upload_button,
            content=ElevatedButton("Upload", on_click=self.upload_files),
            alignment=alignment.center,
            disabled=True,
        )

        return [header, nav_, select_file, body]
