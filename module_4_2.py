def test_function():
    def inner_function():
        nonlocal a

    a = 'Я в области видимости функции test_function'
    print(a)


test_function()
# inner_function() ошибка
