numbers = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]

def foo(x):
    if x >= 50 and not x % 2 == 0:
        return True

print(list(filter(foo, numbers)))