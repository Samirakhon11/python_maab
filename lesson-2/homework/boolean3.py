def  check_positive_even(number):
    is_positive = number >= 0
    is_even = number % 2 == 0

    if is_positive:
        if is_even:
            return "This is a positive and even number"
        else:
            return "This is a positive but and odd number"
    else:
        return "This is not a positive number"

num = int(input("Enter a number: "))
result = check_positive_even(num)

print(result)