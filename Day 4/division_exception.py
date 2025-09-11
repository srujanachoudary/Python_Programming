def fun(a,b):
    try:
        print(a/b)
    except ArithmeticError:
        print('Error: Division by zero is not allowed')
    else:
        print('There is no error')
    finally:
        print('execution completed')
a=10
b=0
fun(a,b)