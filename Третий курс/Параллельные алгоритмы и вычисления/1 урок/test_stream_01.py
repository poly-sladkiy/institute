def small_process():
    print('Testing stream sys.stdin.')
    while True:
        try:
            reply = input('Enter a number > ')

        except EOFError:
            break

    else:
        num = int(reply)
        print("%d squared is %d" % (num, num*num))
    print('Bye')

if __name__ == '__main__':
    small_process()
