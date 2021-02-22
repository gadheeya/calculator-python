from replit import clear
from art import logo

clear()
def add( a1 , b1):
    return a1 + b1

def subtract( a1 , b1):
    return a1 - b1

def multiply( a1 , b1):
    return a1 * b1

def devide( a1 , b1):
    return a1 / b1

caldic = {
    "+":add,
    "-":subtract, 
    "*":multiply,
    "/":devide,
}


totc = 0
fc = True
while 2>1:
    print(logo)
    if fc == True:
        num1 = float(input ("type first number : "))
    else:
        num1 = totc
    for i in caldic:
        print (i)
    opr = input ("pick an operation : ")
    num2 = float(input ("type next number : "))
    totc = (caldic[opr](a1=num1,b1=num2))
    print(f"{num1} {opr} {num2} = {totc}")

    want = input (f"type y to continue with {totc} or type n to start new calculation \n: ")
    if want == "y":
        fc = False
    else :
        clear()