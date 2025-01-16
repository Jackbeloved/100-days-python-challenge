def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

dic ={}
dic["+"] = add
dic["-"] = subtract
dic["*"] = multiply
dic["/"] = divide

import art

end = True
while end:
    print(art.logo)
    result = 0
    n1 = float(input("what is the first number?: "))
    continue_cal = True
    while continue_cal:
        # print("+\n-\n*\n/\n")
        for symbol in dic:
            print(symbol)
        operation = input("Pick an operation: ")
        n2 = float(input("What is the next number: "))
        result = (dic[operation](n1,n2))
        print(n1,operation,n2,"=",result)
        keep = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if keep == "y":
            continue_cal = True
            n1 = result
        else:
            continue_cal = False
            end = True
            print("\n"* 20)