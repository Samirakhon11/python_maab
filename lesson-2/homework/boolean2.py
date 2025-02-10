def check_equal(num1, num2):
    are_equal = num1 == num2
    if are_equal:
        print("They are equal")
    else:
        print("They are not equal")

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

result = check_equal(number1, number2)

print(result)