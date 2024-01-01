import pdb


def my_function():
    x = 5
    y = 10
    z = x + y
    print(z)
    pdb.set_trace() # Встановлюємо точку зупинки breakpoint
    result = z * 2
    print(result)

my_function()