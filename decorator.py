def check_number(f):
    def wrapper(*args):
        if args[0]>0:
            f(args[0])
        elif args[0]<0:
            f(abs(args[0]))
        else :
            f(1)
    return wrapper

@check_number
def multiply(number):
    return number * number
