def my_process():
    import sys

    print('Проверка ------------------------------------\n'
          'приналдежит ли точка с заданными координатами\n'
          'определенной пользователем окружности.')
    print('---------------------------------------------')
    
    # Begin - Подготока данных --------------------------------------
    print('Введите координаты центра окружности')
    
    try:
        A = float(input('X : '))
    except ValueError:
        print('Ошибка ввода данных!')
        sys.exit(1)

    try:
        B = float(input('Y : '))
    except ValueError:
        print('Ошибка ввода данных!')
        sys.exit(1)

    try:
        R = float(input('Величина радиуса R : '))
    
    except ValueError:
        print('Ошибка ввода данных!')
        sys.exit(1)

    # Start of cycle - Начало цикла обработки данных ----------------
    while True:
        try:
            reply = input('Введите через пробел координаты X и Y : ')
        
        except EOFError:
            print('Введено Ctrl-Z')
            break # Пользователь ввел Ctrl+Z – признак

        # завершения ввода данных
        else:
            (x,y) = reply.split(' ')

            try:
                x = float(x)

            except ValueError:
                print('Ошибка ввода данных для координаты X')
                continue

            try:
                y = float(y)

            except ValueError:
                print('Ошибка ввода данных для координаты Y')
                continue

            if (x-A)*(x-A) + (y-B)*(y-B) < R*R:
                print('Точка с координатами (%f,%f) принадлежит'
                      ' указанной окружности' % (x,y))

            else:
                print('Точка с координатами (%f,%f) не принадлежит'
                      ' указанной окружности' % (x,y))
            
            print("Для выхода из цикла нажмите 'Ctrl-Z'")
  
        # End of cycle - Начало цикла обработки данных ------------------
        print('Bye')


if __name__ == '__main__':
    my_process()
