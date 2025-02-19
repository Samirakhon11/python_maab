def check(func):
    def wrapper(a, b):
       if b == 0:
          return "Denominator can't be zero"
       return func(a, b)
    return wrapper

@check
def div(a, b):
   return a / b

while True:
    try:
        a = int(input("Enter a value for a: "))
        break
    except ValueError:
        print("Values can't be empty or non-numeric. Enter a number: ")
    
while True:
    try:
        b = int(input("Enter a value for b: "))
        break
    except ValueError:
        print("Values can't be empty or non-numeric. Enter a number: ")

result = div(a, b)

print(f"Result: {result:.2f}") 