import PySimpleGUI as sg
from ex115.lib import *

layout = [[sg.Text("Cadastro de Pessoas")],
          [sg.Button("OK")],
          [sg.Button("NotOK")],
          [sg.ButtonMenu()]]

# Create the window
window = sg.Window("Demo", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()