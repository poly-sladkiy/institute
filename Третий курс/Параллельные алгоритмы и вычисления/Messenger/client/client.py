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
import requests
import json

HOST = '127.0.0.1'
PORT = 8080
username = ''
companion_username = ''

def new_startup_win():
    layout = [[sg.Text('Welcome! Please, Sign in or Log in if you already have account')],
              [sg.Button('Start chatting')]]
    return sg.Window('Autorization', layout, finalize=True)

def new_log_reg_win():
    layout = [[sg.Text('Login:'), sg.InputText(key = 'l_r_login_key')],
              [sg.Text('Password:'), sg.InputText(key = 'l_r_password_key')],
              [sg.Radio('Log in', '1', default = True, key = 'l_r_radio_log_key'), sg.Radio('Sign in', '1', default = False)],
              [sg.Button('Submit')],
              [sg.Text(size=(15,1), key='l_r_output_err')]]
    return sg.Window('Log/Reg', layout, finalize=True) 

def new_find_win():
    layout = [[sg.Text('Find User')],
              [sg.InputText('admin', key = 'f_username_key')],
              [sg.Button('Find')],
              [sg.Text(size=(15,1), key='f_output_err')]]
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
        if values['l_r_radio_log_key'] == True:
            
            r = requests.post(f'http://{HOST}:{PORT}/login', data={'User-Agent': 'XMessenger', 'username': values['l_r_login_key'], 'password': values['l_r_password_key']})
            data = json.loads(r.content.decode('utf-8'))
            
            if data['request'] == 'OK':
                username = values['l_r_login_key']
                window.close()
                log_reg_win = None
                find_win = new_find_win()

            elif data['request'] == 'BAD':
                window['l_r_output_err'].update('User not found')
        else:
            r = requests.post(f'http://{HOST}:{PORT}/register', data={'User-Agent': 'XMessenger', 'username': values['l_r_login_key'], 'password': values['l_r_password_key']})
            data = json.loads(r.content.decode('utf-8'))
            
            if data['request'] == 'OK':
                username = values['l_r_login_key']
                window.close()
                log_reg_win = None
                find_win = new_find_win()

            elif data['request'] == 'BAD':
                window['l_r_output_err'].update('Something wrong')
        

    elif event == 'Find':
        r = requests.post(f'http://{HOST}:{PORT}/find_user', data={'User-Agent': 'XMessenger', 'username': values['f_username_key']})
        data = json.loads(r.content.decode('utf-8'))
        
        if data['request'] == 'OK':
                companion_username = values['f_username_key']
                if not dialog1_win:
                    dialog1_win = new_dialog1_win()
                elif not dialog2_win:
                    dialog2_win = new_dialog2_win()
                elif not dialog3_win:
                    dialog2_win = new_dialog3_win()

        elif data['request'] == 'BAD':
            window['f_output_err'].update('User not found')
        
    
    elif event == 'Send':
        if dialog1_win:
            print(username + ': ' + values['d1_messege_key'])
            print(companion_username + 'Fuck you, gay')

        elif dialog2_win:
            print(username + ': ' + values['d2_messege_key'])
            print(companion_username + 'Fuck you, gay')

        elif dialog3_win:
            print(username + ': ' + values['d3_messege_key'])
            print(companion_username + ': ' + 'Fuck you, gay')
        

window.close()