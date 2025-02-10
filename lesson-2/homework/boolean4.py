def check_different(num1, num2, num3):
    not_equal1 = num1 != num2
    not_equal2 = num1 != num3
    not_equal3 = num2 != num3

    if not_equal1 and not_equal2 and not_equal3:
        return "All the numbers are different"
    else:
        return "They are not different"
    
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

result = check_different(num1, num2, num3)

print(result)