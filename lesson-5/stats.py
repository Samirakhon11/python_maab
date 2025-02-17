def enrollment_stats(universities):
    students = []
    tuition = []

    for university in universities:
        students.append(university[1])
        tuition.append(university[2])

    return students, tuition

def mean(values):
    return sum(values) / len(values)

def median(values):
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    mid = n // 2

    if n % 2 == 0:
        return (sorted_vals[mid - 1] + sorted_vals[mid]) / 2
    else:
        return sorted_vals[mid]

def main():
    universities = [
        ['California Institute of Technology', 2175, 37704],
        ['Harvard', 19627, 39849],
        ['Massachusetts Institute of Technology', 10566, 40732],
        ['Princeton', 7802, 37000],
        ['Rice', 5879, 35551],
        ['Stanford', 19535, 40569],
        ['Yale', 11701, 40500]
    ]

    students, tuition = enrollment_stats(universities)

    total_students = sum(students)
    total_tuition = sum(tuition)

    student_mean = mean(students)
    student_median = median(students)
    tuition_mean = mean(tuition)
    tuition_median = median(tuition)

    print("******************************")
    print(f"Total students: {total_students:,}")
    print(f"Total tuition: $ {total_tuition:,}")
    print()
    print(f"Student mean: {student_mean:,.2f}")
    print(f"Student median: {student_median}")
    print()
    print(f"Tuition mean: $ {tuition_mean:,.2f}")
    print(f"Tuition median: $ {tuition_median}")
    print("******************************")

if __name__ == "__main__":
    main() 