# import PySimpleGUI as sg
# layout = [
#     [sg.Text('File 1'), sg.InputText(), sg.FileBrowse(),
#      sg.Checkbox('MD5'), sg.Checkbox('SHA1')
#      ],
#     [sg.Text('File 2'), sg.InputText(), sg.FileBrowse(),
#      sg.Checkbox('SHA256')
#      ],
#     [sg.Output(size=(88, 20))],
#     [sg.Submit(), sg.Cancel()]
# ]
# window = sg.Window('File Compare', layout)
# while True:                             # The Event Loop
#     event, values = window.read()
#     # print(event, values) #debug
#     if event in (None, 'Exit', 'Cancel'):
#         break


# import PySimpleGUI as sg

# sg.theme('BluePurple')

# layout_1 = [[sg.Text('That is layout_1')],
#           [sg.Button('Go on layout_2'), sg.Button('Exit')]]

# layout_2 = [[sg.Text('That is layout_2')],
#           [sg.Button('Go on layout_1'), sg.Button('Exit')]]

# window = sg.Window('layout_1', layout_1)

# while True:  # Event Loop
#     event, values = window.read()
#     if event == sg.WIN_CLOSED or event == 'Exit':
#         break

#     if event == 'Go on layout_2':
#         window.close()
#         window = sg.Window('layout_2', layout_2)

#     if event == 'Go on layout_1':
#         window.close()
#         window = sg.Window('layout_1', layout_1)

# window.close()


# import PySimpleGUI as sg
# def open_window():
#     layout = [[sg.Text("New Window", key="new")]]
#     window = sg.Window("Second Window", layout, modal=True)
#     choice = None
#     while True:
#         event, values = window.read()
#         if event == "Exit" or event == sg.WIN_CLOSED:
#             break
        
#     window.close()
# def main():
#     layout = [[sg.Button("Open Window", key="open")]]
#     window = sg.Window("Main Window", layout)
#     while True:
#         event, values = window.read()
#         if event == "Exit" or event == sg.WIN_CLOSED:
#             break
#         if event == "open":
#             open_window()
        
#     window.close()
# if __name__ == "__main__":
#     main()

import PySimpleGUI as sg

"""
    Demo - 2 simultaneous windows using read_all_window
    Window 1 launches window 2
    BOTH remain active in parallel
    Both windows have buttons to launch popups.  The popups are "modal" and thus no other windows will be active
    Copyright 2020 PySimpleGUI.org
"""

def new_startup_win():
    layout = [[sg.Text('Welcome! Please, Sign in or Log in if you already have account')],
              [sg.Button('Start chatting')]]
    return sg.Window('Autorization', layout, finalize=True)

def new_log_reg_win():
    layout = [[sg.Text('Login:'), sg.InputText(key = 'l_r_login_key')],
              [sg.Text('Password:'), sg.InputText(key = 'l_r_password_key')],
              [sg.Radio('Log in', '1', default = True), sg.Radio('Sign in', '1', default = False)],
              [sg.Button('Submit')]]
    return sg.Window('Log/Reg', layout, finalize=True) 

def new_find_win():
    layout = [[sg.Text('Find User')],
              [sg.InputText('admin', key = 'f_username_key')],
              [sg.Button('Find')]]
    return sg.Window('Find User', layout, finalize=True) 

def new_dialog1_win():
    layout = [[sg.Output(size=(88, 20))],
              [sg.InputText('Enter messege', key = 'd1_messege_key')],
              [sg.Button('Send')]]
    return sg.Window('Dialog 1', layout, finalize=True)

def new_dialog2_win():
    layout = [[sg.Output(size=(88, 20))],
              [sg.InputText('Enter messege', key = 'd2_messege_key')],
              [sg.Button('Send')]]
    return sg.Window('Dialog 2', layout, finalize=True)

def new_dialog3_win():
    layout = [[sg.Output(size=(88, 20))],
              [sg.InputText('Enter messege', key = 'd3_messege_key')],
              [sg.Button('Send')]]
    return sg.Window('Dialog 3', layout, finalize=True)

startup_win, log_reg_win, find_win, dialog1_win, dialog2_win, dialog3_win = new_startup_win(), None, None, None, None, None

while True:             # Event Loop
    window, event, values = sg.read_all_windows()

    if event == sg.WIN_CLOSED or event == 'Exit':
        window.close()
        if window == startup_win:
            break
        elif window == startup_win:
            startup_win = None
        elif window == log_reg_win:
            log_reg_win = None
        elif window == find_win:
            find_win = None
        elif window == dialog1_win:
            dialog1_win = None
        elif window == dialog2_win:
            dialog2_win = None
        elif window == dialog3_win:
            dialog3_win = None
    
    elif event == 'Start chatting' and not log_reg_win:
        log_reg_win = new_log_reg_win()

    elif event == 'Submit' and not find_win:
        window.close()
        log_reg_win = None
        find_win = new_find_win()

    elif event == 'Find':
        if not dialog1_win:
            dialog1_win = new_dialog1_win()
        elif not dialog2_win:
            dialog2_win = new_dialog2_win()
        elif not dialog3_win:
            dialog2_win = new_dialog3_win()
    
    elif event == 'Send':
        if dialog1_win.ac:
            print(values['d1_messege_key'])

        elif dialog2_win:
            print(values['d2_messege_key'])

        elif dialog3_win:
            print(values['d3_messege_key'])
        

window.close()