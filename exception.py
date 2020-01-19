def function(a, b):
    print(a / b)


try:
    function(2, 4)
except ZeroDivisionError:
    print('there is a zero here')
finally:
    print("some stupid error")
