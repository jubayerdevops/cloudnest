# simple calculator app

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def pwr(x, y):
    return x ** y

def mod(x, y):
    if y == 0:
        raise ValueError("Cannot perform modulus by zero.")
    return x % y

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Modulus")

    choice = input("Enter choice (1/2/3/4/5/6): ")

    if choice in ['1', '2', '3', '4', '5', '6']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            try:
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")
            except ValueError as e:
                print(e)
        elif choice == '5':
            print(f"{num1} ^ {num2} = {pwr(num1, num2)}")
        elif choice == '6':
            try:
                result = mod(num1, num2)
                print(f"{num1} % {num2} = {result}")
            except ValueError as e:
                print(e)
    else:
        print("Invalid input")

if __name__ == "__main__":
    calculator()