# Setting the desired passing grade
desired_grade = 7.0

# Collecting the student's name and grades
student_name = input("Enter the student's name and press Enter: ")
grade1 = float(input("Enter the student's first grade and press Enter: "))
grade2 = float(input("Enter the student's second grade and press Enter: "))

# Calculating the average of the grades
average = (grade1 + grade2) / 2

# Checking if the average is greater than or equal to the desired passing grade
if average >= desired_grade:
    # If the average is greater than or equal to the desired passing grade, the student is approved
    print("Student", student_name, "is approved. Congratulations!")
else:
    # If the average is less than the desired passing grade, the student is failed
    print("Student", student_name, "is failed. Needs to study more!")
