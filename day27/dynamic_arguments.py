def add(*args):
    sum=0
    for n in args:
        sum += n
    return sum




print(add(2, 3, 4))

def calculate(n,**kwargs):
    print(kwargs)
    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    print(n)
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)
