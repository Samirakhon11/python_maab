def check_divisibility(number):
    if number % 3 == 0 and number % 5 == 0:
        return f"{number} is divisible by both 3 and 5."
    else:
        return f"{number} is not divisible by both 3 and 5."

number = int(input("Enter a number: "))
result = check_divisibility(number)

print(result)