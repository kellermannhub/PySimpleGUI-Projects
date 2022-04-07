import PySimpleGUI as sg


sg.theme("Darkgray10")

layout = [
        [sg.Text("Filename",)],
        [sg.Input(key="-FILE-", text_color="black",
         background_color="white"), sg.FileBrowse(key="-BROWSE-")],
        [sg.Button("Ok", key="-BTNOK-"), sg.Button("Cancel")],
        ]  # Each line it's a line in the interface.

window = sg.Window('First Project', layout, size=(500, 400))


def update_input():
    window["-FILE-"].update("")

while True:
    event, values = window.read()

    # From here we can already see a window and browse files.
    if event == sg.WIN_CLOSED or event == "Cancel":
        print("Window closed.")
        break

    elif event == "-BTNOK-":
        sg.popup(f"The chosen file was: {values['-FILE-']}")
        update_input()  # Cleans the input after user clicks ok.

    print("Event: ", event)
    print("*"*40)


window.close()
