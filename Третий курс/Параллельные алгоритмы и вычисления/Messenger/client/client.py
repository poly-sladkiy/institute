import PySimpleGUI as sg
import requests
import json

HOST = '127.0.0.1'
PORT = 8080
# HOST = '324b-136-169-215-221.ngrok.io'
# PORT = 80
username = ''
companion_username = ''

def new_startup_win():
    layout = [[sg.Text('Welcome! Please, Sign in or Log in if you already have account')],
              [sg.Button('Start chatting')]]
    return sg.Window('Autorization', layout, finalize=True)

def new_connection_win():
    layout = [[sg.Text('Host:'), sg.InputText(key = 'c_host_key')],
              [sg.Text('Port:'), sg.InputText(key = 'c_port_key')],
              [sg.Button('Connect')],
              [sg.Text(size=(15,1), key='c_output_err')]]
    return sg.Window('Log/Reg', layout, finalize=True) 

def new_log_reg_win():
    layout = [[sg.Text('Login:'), sg.InputText(key = 'l_r_login_key')],
              [sg.Text('Password:'), sg.InputText(key = 'l_r_password_key')],
              [sg.Radio('Log in', '1', default = True, key = 'l_r_radio_log_key'), sg.Radio('Sign in', '1', default = False)],
              [sg.Button('Submit')],
              [sg.Text(size=(15,1), key='l_r_output_err')]]
    return sg.Window('Log/Reg', layout, finalize=True) 

def new_find_win():
    layout = [[sg.Text('Find User')],
              [sg.InputText('', key = 'f_username_key')],
              [sg.Button('Find')],
              [sg.Text(size=(15,1), key='f_output_err')]]
    return sg.Window('Find User', layout, finalize=True) 

def new_dialog1_win():
    layout = [[sg.Output(size=(88, 20), key = 'd1_output')],
              [sg.InputText('Enter message', key = 'd1_message_key', do_not_clear = False)],
              [sg.Button('Send'), sg.Button('Check messages')]]
    return sg.Window('Dialog 1', layout, finalize=True)

def new_dialog2_win():
    layout = [[sg.Output(size=(88, 20), key = 'd2_output')],
              [sg.InputText('Enter message', key = 'd2_message_key', do_not_clear = False)],
              [sg.Button('Send'), sg.Button('Check messages')]]
    return sg.Window('Dialog 2', layout, finalize=True)

def new_dialog3_win():
    layout = [[sg.Output(size=(88, 20), key = 'd3_output')],
              [sg.InputText('Enter message', key = 'd3_message_key', do_not_clear = False)],
              [sg.Button('Send'), sg.Button('Check messages')]]
    return sg.Window('Dialog 3', layout, finalize=True)

startup_win, connection_win,  log_reg_win, find_win, dialog1_win, dialog2_win, dialog3_win = new_startup_win(), None, None, None, None, None, None

while True:             # Event Loop
    window, event, values = sg.read_all_windows()

    if event == sg.WIN_CLOSED or event == 'Exit':
        window.close()
        if window == startup_win:
            break
        elif window == startup_win:
            startup_win = None
        elif window == connection_win:
            connection_win = None
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
            print(username + ': ' + values['d1_message_key'])
            r = requests.post(f'http://{HOST}:{PORT}/send_to', data={'User-Agent': 'XMessenger', 'from': username, 'to': companion_username, 'msg': values['d1_message_key']})

        elif dialog2_win:
            print(username + ': ' + values['d2_message_key'])
            r = requests.post(f'http://{HOST}:{PORT}/send_to', data={'User-Agent': 'XMessenger', 'from': username, 'to': companion_username, 'msg': values['d2_message_key']})

        elif dialog3_win:
            print(username + ': ' + values['d3_message_key'])
            r = requests.post(f'http://{HOST}:{PORT}/send_to', data={'User-Agent': 'XMessenger', 'from': username, 'to': companion_username, 'msg': values['d3_message_key']})


    elif event == 'Check messages':
        if dialog1_win:
            r = requests.get(f'http://{HOST}:{PORT}/check_messages', params={'User-Agent': 'XMessenger', 'username': username})
            data = json.loads(r.content.decode('utf-8'))

            if data['request'] == 'OK':
                window['d1_output'].update('')
                for msg in data['data']:
                    if msg['from'] == companion_username:
                        print(companion_username + ': ' + msg['msg'])

            elif data['request'] == 'BAD':
                window['d1_output'].update('')
                print('FATAL ERROR! Nobody wants to write you')

        elif dialog2_win:
            r = requests.get(f'http://{HOST}:{PORT}/check_messages', params={'User-Agent': 'XMessenger', 'username': username})
            data = json.loads(r.content.decode('utf-8'))

            if data['request'] == 'OK':
                window['d2_output'].update('')
                for msg in data['data']:
                    if msg['from'] == companion_username:
                        print(companion_username + ': ' + msg['msg'])

            elif data['request'] == 'BAD':
                window['d2_output'].update('')
                print('FATAL ERROR! Nobody wants to write you')

        elif dialog3_win:
            r = requests.get(f'http://{HOST}:{PORT}/check_messages', params={'User-Agent': 'XMessenger', 'username': username})
            data = json.loads(r.content.decode('utf-8'))

            if data['request'] == 'OK':
                window['d3_output'].update('')
                for msg in data['data']:
                    if msg['from'] == companion_username:
                        print(companion_username + ': ' + msg['msg'])

            elif data['request'] == 'BAD':
                window['d3_output'].update('')
                print('FATAL ERROR! Nobody wants to write you')
        

window.close()