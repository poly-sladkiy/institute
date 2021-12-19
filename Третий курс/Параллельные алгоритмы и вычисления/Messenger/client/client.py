import PySimpleGUI as sg
import requests
import json

HOST = '127.0.0.1'
PORT = 8080
username = ''
companion_username = ''
msg_arr = []
win_number = 0


# --------------------| Windows |-------------------- #

def new_startup_win():
    layout = [[sg.Text('Welcome! Please, Sign in or Log in if you already have account')],
              [sg.Button('Start chatting')]]
    return sg.Window('Autorization', layout, finalize=True)

def new_connection_win():
    layout = [[sg.Text('Host:', size=(7,1)), sg.InputText(key = 'c_host_key')],
              [sg.Text('Port:', size=(7,1)), sg.InputText(key = 'c_port_key')],
              [sg.Checkbox('Default', key = 'c_cb')],
              [sg.Button('Connect')],
              [sg.Text(size=(15,1), key='c_output_err', text_color = 'red')]]
    return sg.Window('Connection', layout, finalize=True) 

def new_log_reg_win():
    layout = [[sg.Text('Login:', size=(10,1)), sg.InputText(key = 'l_r_login_key')],
              [sg.Text('Password:', size=(10,1)), sg.InputText(key = 'l_r_password_key', password_char = '*')],
              [sg.Radio('Log in', '1', default = True, key = 'l_r_radio_log_key'), sg.Radio('Sign in', '1', default = False)],
              [sg.Button('Submit')],
              [sg.Text(size=(15,1), key='l_r_output_err', text_color = 'red')]]
    return sg.Window('Log/Reg', layout, finalize=True) 

def new_find_win():
    layout = [[sg.Text(size=(15,1), key='f_output_name', justification = 'center')],
              [sg.Text('Find User')],
              [sg.InputText('', key = 'f_username_key')],
              [sg.Button('Find')],
              [sg.Text(size=(15,1), key='f_output_err', text_color = 'red')]]
    return sg.Window('Find User', layout, finalize=True) 

def new_dialog1_win():
    layout = [[sg.Text(size=(15,1), key='d1_output_name', justification = 'center')],
              [sg.Output(size=(88, 20), key = 'd1_output')],
              [sg.InputText('Enter message', key = 'd1_message_key', do_not_clear = False)],
              [sg.Button('Send 1'), sg.Button('Check messages 1')],
              [sg.Text(size=(15,1), key='d1_output_err', text_color = 'red')]]
    return sg.Window('Dialog 1', layout, finalize=True)

def new_dialog2_win():
    layout = [[sg.Text(size=(15,1), key='d2_output_name', justification = 'center')],
              [sg.Output(size=(88, 20), key = 'd2_output')],
              [sg.InputText('Enter message', key = 'd2_message_key', do_not_clear = False)],
              [sg.Button('Send 2'), sg.Button('Check messages 2')],
              [sg.Text(size=(15,1), key='d2_output_err', text_color = 'red')]]
    return sg.Window('Dialog 2', layout, finalize=True)

def new_dialog3_win():
    layout = [[sg.Text(size=(15,1), key='d3_output_name', justification = 'center')],
              [sg.Output(size=(88, 20), key = 'd3_output')],
              [sg.InputText('Enter message', key = 'd3_message_key', do_not_clear = False)],
              [sg.Button('Send 3'), sg.Button('Check messages 3', text_color = 'red')],
              [sg.Text(size=(15,1), key='d3_output_err')]]
    return sg.Window('Dialog 3', layout, finalize=True)

def new_connection_err_win():
    layout = [[sg.Text('Connection error!')],
              [sg.Button('Back to connection')]]
    return sg.Window('Connection error', layout, finalize=True)


startup_win, connection_win,  log_reg_win, find_win, dialog1_win, dialog2_win, dialog3_win, connection_err_win = new_startup_win(), None, None, None, None, None, None, None

# --------------------| Functions |-------------------- #

def send(n):
    try:
        if values['d' + str(n) + '_message_key'] != '':
            print(username + ': ' + values['d' + str(n) + '_message_key'])
            r = requests.post(f'http://{HOST}:{PORT}/send_to', data={'User-Agent': 'XMessenger', 'from': username, 'to': companion_username, 'msg': values['d' + str(n) + '_message_key']})
        else:
            window['d' + str(n) + '_output_err'].update('Empty messege')
    
    except (requests.exceptions.InvalidURL, requests.exceptions.ConnectionError) as er:
                window.close()
                connection_err_win = new_connection_err_win()

def check_msg(n):
    try:
        r = requests.get(f'http://{HOST}:{PORT}/check_messages', params={'User-Agent': 'XMessenger', 'username': username})
        data = json.loads(r.content.decode('utf-8'))

        msg_arr = []
        if data['request'] == 'OK':
            window['d' + str(n) + '_output'].update('')
            for msg in data['data']:
                if msg['from'] == companion_username:
                    msg_arr.append(msg)
                if username != companion_username:
                    if (msg['from'] == username) and (msg['to'] == companion_username):
                        msg_arr.append(msg)

            for a in sorted(msg_arr, key = lambda x: x['time']):
                print('[' + a['time'] + '] ' + a['from'] + ': ' + a['msg'])

        elif data['request'] == 'BAD':
            window['d' + str(n) + '_output'].update('')
            print('FATAL ERROR! Nobody wants to write you')
    
    except (requests.exceptions.InvalidURL, requests.exceptions.ConnectionError) as er:
                window.close()
                connection_err_win = new_connection_err_win()

while True:             # Event Loop
    window, event, values = sg.read_all_windows()

    if event == sg.WIN_CLOSED or event == 'Back to connection':
        window.close()
        if window == startup_win:
            break
        elif window == startup_win:
            startup_win = None
        elif window == connection_err_win:
            window.close()
            connection_err_win = None
            dialog1_win = None
            dialog2_win = None
            dialog3_win = None
            find_win = None
            log_reg_win = None
            connection_win = new_connection_win()
        elif window == connection_win:
            connection_win = None
        elif window == log_reg_win:
            log_reg_win = None
        elif window == find_win:
            find_win = None
        elif window == dialog1_win:
            dialog1_win = None
            win_number -= 1
        elif window == dialog2_win:
            dialog2_win = None
            win_number -= 1
        elif window == dialog3_win:
            dialog3_win = None
            win_number -= 1
    
    elif event == 'Start chatting' and not connection_win:
        connection_win = new_connection_win()


    elif event == 'Connect' and not log_reg_win:
        try:
            if values['c_cb'] == True:
                HOST = '127.0.0.1'
                PORT = 8080
                window.close()
                connection_win = None
                log_reg_win = new_log_reg_win()
            else:
                if (values['c_host_key'] != '') and (values['c_port_key'] != ''):
                    HOST = values['c_host_key']
                    PORT = values['c_port_key']
                    r = requests.get(f'http://{HOST}:{PORT}')
                    window.close()
                    connection_win = None
                    log_reg_win = new_log_reg_win()
                else:
                    window['c_output_err'].update('Empty field')
        
        except (requests.exceptions.InvalidURL, requests.exceptions.ConnectionError) as er:
                window.close()
                connection_err_win = new_connection_err_win()


    elif event == 'Submit' and not find_win:
        try:
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

        except (requests.exceptions.InvalidURL, requests.exceptions.ConnectionError) as er:
                window.close()
                connection_err_win = new_connection_err_win()
        

    elif event == 'Find':
        try:
            window['f_output_name'].update('Hi ' + username)
            if win_number != 3:
                r = requests.post(f'http://{HOST}:{PORT}/find_user', data={'User-Agent': 'XMessenger', 'username': values['f_username_key']})
                data = json.loads(r.content.decode('utf-8'))
                
                if data['request'] == 'OK':
                        companion_username = values['f_username_key']
                        if not dialog1_win:
                            win_number += 1
                            dialog1_win = new_dialog1_win()
                        elif not dialog2_win:
                            win_number += 1
                            dialog2_win = new_dialog2_win()
                        elif not dialog3_win:
                            win_number += 1
                            dialog2_win = new_dialog3_win()

                elif data['request'] == 'BAD':
                    window['f_output_err'].update('User not found')

        except (requests.exceptions.InvalidURL, requests.exceptions.ConnectionError) as er:
                window.close()
                connection_err_win = new_connection_err_win()
        

    elif event == 'Send 1':
        window['d1_output_name'].update(companion_username)
        send(1)
    elif event == 'Send 2':
        window['d2_output_name'].update(companion_username)
        send(2)
    elif event == 'Send 3':
        window['d3_output_name'].update(companion_username)
        send(3)

    elif event == 'Check messages 1':
        check_msg(1)
    elif event == 'Check messages 2':
        check_msg(2)
    elif event == 'Check messages 3':
        check_msg(3)       

window.close()