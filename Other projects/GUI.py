import PySimpleGUI as sg

# Define the window's contents
layout = [[sg.Button('', button_color=('#FFFFFF', '#FF0000'), enable_events=True, key='FF0000'),
           sg.Button('', button_color=('#FFFFFF', '#00FF00'),
                     enable_events=True, key='00FF00'),
           sg.Button('', button_color=('#FFFFFF', '#0000FF'), enable_events=True, key='0000FF')],

          [sg.Button('', button_color=('#FFFFFF', '#FFFFFF'), enable_events=True, key='FFFFFF'),
           sg.Button('', button_color=('#FFFFFF', '#808080'),
                     enable_events=True, key='808080'),
           sg.Button('', button_color=('#FFFFFF', '#FFFF00'), enable_events=True, key='FFFF00')]]


# Create the window
window = sg.Window('Window Title', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    print(values, event)
    if event == 'but':
        print('hi')
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    # window['-OUTPUT-'].update('Hello ' + values['-INPUT-'] + "! Thanks for trying PySimpleGUI")

# Finish up by removing from the screen
window.close()
