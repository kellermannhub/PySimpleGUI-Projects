import PySimpleGUI as sg


layout = [
        [sg.Text('Filename')],
        [sg.Input(), sg.FileBrowse()],
        [sg.Button('Ok'), sg.Button('Cancel')]
        ]  # Each line it's a line in the interface.

window = sg.Window('First Project', layout)

event, values = window.read()

window.close()  # From here we can already see a window and browse files.
