import PySimpleGUI as sg


def create_main_window(title, theme="darkgrey5"):
    # Theme
    sg.theme(theme)
    # Layout
    layout = [
        [
            sg.Text("Hello world!")
        ]
        ]

    # Window title
    title = title

    # Creating window
    window = sg.Window(title, layout)

    return window

window = create_main_window("Basic template")

# Main loop
while True:
    event, values = window.read()

    # Breaking the loop
    if event == sg.WINDOW_CLOSED:
        break

window.close()
