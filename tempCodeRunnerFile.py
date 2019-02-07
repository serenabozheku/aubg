def add(x, y):
    return x+y


def substract(x, y):
    return x-y


def multiply(x, y):
    return x*y


def divide(x, y):
    return x/y


def sumcount(list):
    sum = 0
    for x in list:
        sum += x
    return sum


print("Operation to perform: ")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
print("5. Count and sum a bunch of numbers")


operation = input("Select operations 1, 2, 3, 4, 5")


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if operation == "1":
    print(add(num1, num2))


elif operation == "2":
    print(substract(num1, num2))


elif operation == "3":
    print(multiply(num1, num2))


elif operation == "4":
    print(divide(num1, num2))


elif operation == "5":
    input_string = input("Enter a list element separated by ',' ")
    list = input_string.split(",")
    print("Calculating sum and count of element of input list")
    sum = 0
    for num in list:
        sum += int(num)
    print("Sum = ", sum)
    print("You entered ", len(list), "element/s.")
