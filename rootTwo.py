import sys

def main():
    quit = True;
    while quit:
        num = input("Enter a number: ")
        if num == "q" or num == "Q":
            sys.exit()
        num = float(num)
        print(newtonsMethod(num, 20))

def newtonsMethod(a, iter):
    x = a
    for i in range(iter):
        f = x*x - a
        fDerivative = 2*x
        x = x - f/fDerivative
    return x

main()

