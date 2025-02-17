def convert_cel_to_far(degrees_cel):
    return degrees_cel * (9 / 5) + 32

def convert_far_to_cel(degrees_far):
    return (degrees_far - 32) * (5 / 9)

degrees_f = float(input("Enter a temperature in degrees F: "))
result1 = convert_far_to_cel(degrees_f)

print(f"{degrees_f} degrees F = {result1:.2f} degrees C")

degrees_c = float(input("Enter a temperature in degrees C: "))
result2 = convert_cel_to_far(degrees_c)
print(f"{degrees_c} degrees C = {result2:.2f} degrees F")