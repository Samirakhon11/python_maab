import csv
from collections import defaultdict

def read_grades(filename):
    grades = defaultdict(list)
    with open('grades.csv', 'rt') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row) 
            subject = row["Subject"]
            try:
                grade = float(row["Grade"])  
                grades[subject].append(grade)
            except ValueError:
                print(f"Skipping invalid grade: {row['Grade']} for subject {subject}")
    return grades

def calculate_average_grade(grades):
    averages = {subject: sum(marks) / len(marks) for subject, marks in grades.items()}

    return averages

def write_average(filename, averages):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Subject", "Average Grade"])
        for subject, avg in averages.items():
            writer.writerow([subject, round(avg, 1)])

grades_data = read_grades("grades.csv")
average_grades = calculate_average_grade(grades_data)
write_average("average_grades.csv", average_grades)