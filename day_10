from art import logoCalculator
from replit import clear


#show logo
print(logoCalculator)


#functions to for arthimetic operations

def add(num1, num2): #addition function
    return num1 + num2

def subtract(num1, num2): #subtraction function
    return num1 - num2

def multiply(num1, num2): #multiply function
    return num1 * num2
             
def divide(num1, num2): #divide function
    return num1 / num2


#dictionary linking symbol to function
operationFUNCTION ={"+": add,"-":subtract,"*":multiply,"/":divide}


toCONTINUE = True

#while not statement to conduct 
while toCONTINUE:
    num1 = int(input("Enter your the first number: "))
    print('''What is your function:
                    "+": add  
                    "-":subtract
                    "*":multiply
                    "/":divide: ''')
    operatorSYMBOL=input()
    num2 = int(input("Enter your second number"))

    answer = operationFUNCTION[operatorSYMBOL](num1,num2)
    print(f"{num1} {operatorSYMBOL} {num2} = {answer}")
    
    wantCONTINUE = input("Do you want to continue: y/n")
    if wantCONTINUE.lower() == "n":
        toCONTINUE=False
    else:
        clear()











