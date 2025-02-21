import math

class Vector:
    def __init__(self, *components):
        self.components = tuple(components)

    def __repr__(self):
        return f"VectornD({', '.join(map(str, self.components))})"
    
    def __add__(self, other):
        if not isinstance(other, Vector) or len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimention for addition!")
        return Vector(*[a + b for a, b in zip(self.components, other.components)])
    
    def __sub__(self, other):
        if not isinstance(other, Vector) or len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimention for subtraction!")
        return Vector(*[a - b for a, b, in zip(self.components, other.components)])
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(*[a * other for a in self.components])
        elif isinstance(other, Vector):
            if len(self.components) != len(other.components):
                raise ValueError("Vectors must have the same dimensions for dot product!")
            return sum(a * b for a, b in zip(self.components, other.components))
        else:
            raise TypeError("Multiplication not supported between instances of 'Vector' and non-numeric/non-Vector type.")
        
    def __rmul__(self, other):
        return self.__mult__(other)
    
    def magnitude(self):
        return math.sqrt(sum(a ** 2 for a in self.components))
    
    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector.")
        return Vector(*[a / mag for a in self.components])
    
@staticmethod
def create_vector_from_input():
    while True:
        try:
            dimension = int(input("Enter the dimension of the vector: "))
            if dimension <= 0:
                raise ValueError("Dimension must be a positive integer.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid positive integer.")

    components = []
    for i in range(dimension):
        while True:
            try:
                value = float(input(f"Enter component {i + 1}: "))
                components.append(value)
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

    return Vector(*components)  

print("Enter the first vector:")
v1 = Vector.create_vector_from_input()

print("Enter the second vector:")
v2 = Vector.create_vector_from_input()

while True:
    try:
        scalar = float(input("Enter a scalar number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

print("\nFirst vector:", v1)
print("Second vector:", v2)
print("Sum:", v1 + v2)
print("Difference:", v1 - v2)
print("Dot Product:", v1 * v2)
print(f"First vector multiplied by {scalar}:", v1 * scalar)
print(f"Second vector multiplied by {scalar}:", v2 * scalar)
