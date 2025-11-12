# ------------------------------------------------------------
# Daily Calorie Tracker CLI
# Author: Ananya Agrawal
# Date: 10-Nov-2025
# Course: Programming for Problem Solving using Python
# ------------------------------------------------------------
# Description:
# A simple command-line tool to record meals and calorie intake,
# compare it against a daily calorie limit, and optionally save
# the session log to a text file.
# ------------------------------------------------------------

# Task 1: Setup & Introduction
print("--------------------------------------------------")
print("Welcome to the Daily Calorie Tracker CLI!")
print("This tool helps you log your meals and track total calorie intake.")
print("--------------------------------------------------")

# Task 2: Input & Data Collection
meals = [] # list to store meal names
calories = [] # list to store calorie values

num_meals = int(input("\nHow many meals did you have today? "))

for i in range(num_meals):
    meal_name = input(f"Enter name of meal {i+1} (e.g., Breakfast): ")
    calorie_amt = float(input(f"Enter calories for {meal_name}: "))
    meals.append(meal_name)
    calories.append(calorie_amt)

# Task 3: Calorie Calculations
total_calories = sum(calories)
average_calories = total_calories / len(calories)

daily_limit = float(input("\nEnter your daily calorie limit: "))

# Task 4: Exceed Limit Warning System
if total_calories > daily_limit:
    limit_status = "⚠️ You have exceeded your daily calorie limit!"
else:
    limit_status = "✅ Great! You are within your daily calorie limit."

# Task 5: Neatly Formatted Output
print("\n--------------------------------------------------")
print("Summary of Today's Calorie Intake")
print("--------------------------------------------------")
print(f"{'Meal Name':<15} {'Calories':>10}")
print("-" * 30)

for i in range(len(meals)):
    print(f"{meals[i]:<15} {calories[i]:>10.2f}")

print("-" * 30)
print(f"{'Total':<15} {total_calories:>10.2f}")
print(f"{'Average':<15} {average_calories:>10.2f}")
print("--------------------------------------------------")
print(limit_status)
print("--------------------------------------------------")

# Task 6 (Bonus): Save Session Log to File
save_option = input("\nDo you want to save this session to a file? (yes/no): ").strip().lower()

if save_option == "yes":
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"calorie_log_{timestamp}.txt"

    with open(filename, "w") as f:
        f.write("Daily Calorie Tracker CLI - Session Log\n")
        f.write(f"Author: Ananya Agrawal\n")
        f.write(f"Timestamp: {timestamp}\n")
        f.write("--------------------------------------------------\n")
        f.write(f"{'Meal Name':<15} {'Calories':>10}\n")
        f.write("-" * 30 + "\n")
        for i in range(len(meals)):
            f.write(f"{meals[i]:<15} {calories[i]:>10.2f}\n")
        f.write("-" * 30 + "\n")
        f.write(f"{'Total':<15} {total_calories:>10.2f}\n")
        f.write(f"{'Average':<15} {average_calories:>10.2f}\n")
        f.write("--------------------------------------------------\n")
        f.write(limit_status + "\n")

    print(f"\nSession successfully saved as '{filename}' ✅")
else:
    print("\nSession not saved. Goodbye! 👋")

# End of Program
