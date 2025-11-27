# Student Grade Analyzer
# This program allows users to manage student grades, generate reports, and find the top student.

students: list[dict[str, list[int]]] = [] # List to hold student records

# Function to add grades for a student
def add_grade() -> None:
    """
    Add grades to an existing student in the students list."""
    name = input("Enter student name: ")
    for student in students:
        if name in student.keys():
            while True:
                data = input("Enter a grade (or 'done' to finish): ")
                try:
                    grade = int(data)
                    if 0 <= grade <= 100:
                        student[name].append(grade)
                    else:
                        print("Grade must be between 0 and 100.")
                except ValueError:
                    if data.lower() == 'done':
                        return
                    else:
                        print("Invalid input. Please enter a number.")
    print("Student not found.")

# Function to add a new student
def add_student() -> None:
    """
    Add a new student to the students list if they do not already exist.
    """
    name = input("Enter student name: ")
    if not name:
        print("Name cannot be empty.")
        return
    if name[0] not in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
        print("Name must start with a letter.")
        return
    if any(name in student.keys() for student in students):
        print("Student already exists.")
    else:
        student: dict[str, list[int]] = {name: []}
        students.append(student)

# Function to generate and display report
def show_report() -> None:
    """
    Generate and display a report of all students with their average grades, 
    maximum average, minimum average, and overall average.
    """
    print("--- Student Report ---")
    max_avg = -1
    min_avg = 101
    all_grades_cnt = 0
    all_grades = 0
    if students:
        for student in students:
            name, grades = next(iter(student.items()))
            avg: float | str
            try:
                avg = sum(grades) / len(grades)
                all_grades += sum(grades)
                all_grades_cnt += len(grades)
                max_avg = max(max_avg, avg)
                min_avg = min(min_avg, avg)

            except ZeroDivisionError:
                avg = "N/A"
            if isinstance(avg, float):
                print(f"{name}'s average grade is {avg:.1f}")
            else:
                print(f"{name}'s average grade is {avg}")
        try:
            overall_avg = all_grades / all_grades_cnt
            print('-' * 26)
            print(f"Max Average: {max_avg:.1f}")
            print(f"Min Average: {min_avg:.1f}")
            print(f"Overall Average: {overall_avg:.1f}")
        except ZeroDivisionError:
            print("There are no grades.")
        
    else:
        print("There are no students.")

# Function to find and display the top student
def find_top_student() -> None:
    """
    Find and display the student with the highest average grade.
    """
    if students:
        best = max(
            students,
            key=lambda student: sum(grades) / len(grades)
            if (grades := next(iter(student.values())))
            else -1
        )
        name, grades = next(iter(best.items()))
        try:
            avg = sum(grades) / len(grades)
            print(f"The student with highest average is {name} with a grade of {avg:.1f}")
        except ZeroDivisionError:
            print("There are no grades for the top student.")
    else:
        print("There are no students.")
            


# Main program loop
while True:
    try:
        choice = int(input("""--- Student Grade Analyzer ---
1. Add a new student
2. Add grades for a student
3. Generate a full report
4. Find the top student
5. Exit program
Enter your choice: """))
        match choice:
            case 1:
                add_student()
            case 2:
                add_grade()
            case 3:
                show_report()
            case 4:
                find_top_student()
            case 5:
                print("Exiting program.")
                break
    
    except ValueError:
        print("Invalid input. Please enter a number corresponding to the options.")
    print()