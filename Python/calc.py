# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x-y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

def selection():
    print('''==========================''')
    print('''   Select the operation''')
    print("        1 - Add")
    print("        2 - Subtract")
    print("        3 - Multiply")
    print("        4 - Divide")
    print("        5 - Exit")
    print('''==========================''')
    

while True:
    # take input from the user
    selection()
    choice = int(input("Enter the choice: "))
    if choice==1:
        print("<----------Addition---------->")
        print("Enter the numbers you want to add")
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        print(f"The sum is: {x+y}")
    
    elif choice==2:
        print("<---------Subtraction--------->")
        print("Enter the numbers you want to subtract")
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        print(f"The sum is: {x-y}")
    
    elif choice==3:
        print("<---------Multiplication--------->")
        print("Enter the numbers you want to multiply")
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        print(f"The sum is: {x*y}")
    
    elif choice==4:
        print("<---------Division--------->")
        print("Enter the numbers you want to divide")
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        print(f"The sum is: {x/y}")

    elif choice==5:
        print("<---------Exiting--------->")
        break
    else:
        print("Invalid Option selected")
