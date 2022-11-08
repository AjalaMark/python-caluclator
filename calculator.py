def add(a,b):
    answer = a + b
    print(str(a) + "+" + str(b) + " = "  + str(answer))

def subtract(a,b):
    answer = a-b
    print(str(a) + "-" + str(b) + " = "  + str(answer))

def multiply(a,b):
    answer = a*b
    print(str(a) + "*" + str(b) + " = "  + str(answer))

def divide(a,b):
    answer = a/b
    print(str(a) + "/" + str(b) + " = "  + str(answer))

while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")

    choice = input("choose math operation: ")

    if choice == "A" or choice == "a":
        firstNumber = int(input("input first number: "))
        secondNumber = int(input("input secodn number: "))
        add(firstNumber, secondNumber)
    elif choice == "B" or choice == "b":
        firstNumber = int(input("input first number: "))
        secondNumber = int(input("input secodn number: "))
        subtract(firstNumber, secondNumber)
    elif choice == "C" or choice == "c":
        firstNumber = int(input("input first number: "))
        secondNumber = int(input("input secodn number: "))
        multiply(firstNumber, secondNumber)
    elif choice == "D" or choice == "d":
        firstNumber = int(input("input first number: "))
        secondNumber = int(input("input secodn number: "))
        divide(firstNumber, secondNumber)
    else:
        print("program has ended")
        quit()


