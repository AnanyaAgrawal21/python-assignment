# -------------------------------
# Task 1: Menu Display
# -------------------------------
def display_menu():
    print("\n==============================")
    print("GRADEBOOK ANALYZER")
    print("==============================")
    print("1. Enter student data manually")
    print("2. Load data from CSV file")
    print("3. Exit")
    print("==============================")

# -------------------------------
# Task 2: Data Entry or CSV Input
# -------------------------------
def manual_input():
    marks = {}
    n = int(input("Enter number of students: "))
    for _ in range(n):
        name = input("Enter student name: ")
        mark = float(input(f"Enter marks for {name}: "))
        marks[name] = mark
    return marks

def load_from_csv():
    marks = {}
    filename = input("Enter CSV filename (with .csv extension): ")
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) >= 2:
                    try:
                        marks[row[0]] = float(row[1])
                    except:
                        pass
        print("Data loaded successfully from CSV.")
    except:
        print("Error: Could not open file.")
    return marks

# -------------------------------
# Task 3: Statistical Functions
# -------------------------------
def calculate_average(marks):
    total = sum(marks.values())
    return total / len(marks)

def calculate_median(marks):
    values = sorted(marks.values())
    n = len(values)
    mid = n // 2
    if n % 2 == 0:
        return (values[mid - 1] + values[mid]) / 2
    else:
        return values[mid]

def find_max_score(marks):
    return max(marks.values())

def find_min_score(marks):
    return min(marks.values())

# -------------------------------
# Task 4: Grade Assignment
# -------------------------------
def assign_grades(marks):
    grades = {}
    for name, mark in marks.items():
        if mark >= 90:
            grades[name] = "A"
        elif mark >= 80:
            grades[name] = "B"
        elif mark >= 70:
            grades[name] = "C"
        elif mark >= 60:
            grades[name] = "D"
        else:
            grades[name] = "F"
    return grades

def grade_distribution(grades):
    dist = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for g in grades.values():
        dist[g] += 1
    return dist

# -------------------------------
# Task 5: Pass/Fail Lists
# -------------------------------
def pass_fail_lists(marks):
    passed = [n for n, m in marks.items() if m >= 40]
    failed = [n for n, m in marks.items() if m < 40]
    return passed, failed

# -------------------------------
# Task 6: Table Output and Loop
# -------------------------------
def display_table(marks, grades):
    print("\n-------------------------------")
    print(f"{'Name':<15}{'Marks':<10}{'Grade':<5}")
    print("-------------------------------")
    for name in marks:
        print(f"{name:<15}{marks[name]:<10.2f}{grades[name]:<5}")
    print("-------------------------------")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            marks = manual_input()
        elif choice == "2":
            marks = load_from_csv()
        elif choice == "3":
            print("Exiting GradeBook Analyzer.")
            break
        else:
            print("Invalid choice, try again.")
            continue

        if not marks:
            print("No data available.")
            continue

        avg = calculate_average(marks)
        med = calculate_median(marks)
        high = find_max_score(marks)
        low = find_min_score(marks)

        print("\nSTATISTICAL SUMMARY")
        print(f"Average: {avg:.2f}")
        print(f"Median : {med:.2f}")
        print(f"Highest: {high}")
        print(f"Lowest : {low}")

        grades = assign_grades(marks)
        dist = grade_distribution(grades)
        print("\nGRADE DISTRIBUTION:")
        for g, c in dist.items():
            print(f"{g}: {c} student(s)")

        passed, failed = pass_fail_lists(marks)

        print("\nPASSED STUDENTS:")
        if passed:
            for name in passed:
                print(name)
        else:
            print("None")

        print("\nFAILED STUDENTS:")
        if failed:
            for name in failed:
                print(name)
        else:
            print("None")

        display_table(marks, grades)

        again = input("\nDo you want to analyze again? (y/n): ").lower()
        if again != "y":
            print("Exiting GradeBook Analyzer.")
            break

if __name__ == "__main__":
main()