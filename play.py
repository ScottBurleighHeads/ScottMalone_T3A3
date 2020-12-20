def multiply(*args):
    z = 1
    for num in args:
        z *= num
    print(z)

multiply(4, 5)
multiply(10, 9)
multiply(2, 3, 4)
multiply(3, 5, 10, 6)

def print_kwargs(**kwargs):
        for key,value in kwargs.items():
            print(f"key = {key}, value = {value}")

print_kwargs(kwargs_1="Shark", kwargs_2=4.5, kwargs_3=True)