def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y



def main():
    print("Choose what you want to do:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")


    choice = input("Enter choice (1/2/3): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
