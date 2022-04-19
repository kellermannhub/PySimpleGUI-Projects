import os
import pathlib
import PySimpleGUI as pg


def create_main_window(title, theme="darkgrey5"):
    # Theme
    pg.theme(theme)
    # Layout
    layout = [
        [
            pg.Text("Text editor"),
        ],
        [
            pg.Text("File name:"),
            pg.Input(key="-NAME-"),
            pg.Radio(".py", group_id="extension", default=True, key="-PY-"),
            pg.Radio(".txt", group_id="extension", key="-TXT-"),
        ],
        [
            pg.Multiline(size=(150, 30), key="-CONTENT-")
        ],
        [
            pg.Button("Save file", size=(150-17, None), key="-SAVE-")
        ],
            ]

    # Window title
    title = title

    # Creating window
    window = pg.Window(title, layout, element_justification="center")

    return window


window = create_main_window("Basic Text Editor")


# Main loop
while True:
    event, values = window.read()

    if event == '-SAVE-':
        if values['-PY-']:
            extension = ".py"

        else:
            extension = ".txt"

        filename = values['-NAME-'] + extension
        content = values['-CONTENT-']

        parent_directory = pathlib.Path(__file__).parent.resolve()

        folder = "saved files"
        path = os.path.join(parent_directory, folder)

        if not os.path.isdir(path):
            os.makedirs(path)

        full_path = os.path.join(path, filename)

        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)

    # Breaking the loop
    if event == pg.WINDOW_CLOSED:
        break

window.close()
