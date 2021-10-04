import _thread

def function(x):
    print('%d ^ 12 = %d\n' % (x, x ** 12))


class AnyClass:
    def __init__(self, x):
        self.x = x

    def function(self):
        print('%d ^ 12 = %d\n' % (self.x, self.x**12))
# END class AnyClass


# передача параметра - ссылки
_thread.start_new_thread(function, (3,))

# передача параметра – lambda-выражения
_thread.start_new_thread((lambda: function(3)), ())

obj = AnyClass(3)

# передача параметра – ссылки на связанный метод
_thread.start_new_thread(obj.function, ())

print('Main process exiting.\n')
