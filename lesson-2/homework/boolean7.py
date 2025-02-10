def check_sum(num1, num2):
    total = num1 + num2
    if total > 50.8:
        return "The sum is greater than 50.8."
    else:
        return "The sum is not greater than 50.8."

def check_range(number):
    if 10 <= number <= 20:
        return "The number is between 10 and 20 (inclusive)."
    else:
        return "The number is not between 10 and 20."

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

result_sum = check_sum(number1, number2)

print(result_sum)

user_number = float(input("Enter a number to check if it's between 10 and 20: "))

result_range = check_range(user_number)

print(result_range)