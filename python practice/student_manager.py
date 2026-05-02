import csv

def add_student():
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))

    with open("students.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, marks])

    print("Student added!")

def view_students():
    try:
        with open("students.csv", "r") as file:
            reader = csv.reader(file)
            print("\nStudent List:")
            for row in reader:
                print("Name:", row[0], "| Marks:", row[1])
    except:
        print("No data found")

def average_marks():
    total = 0
    count = 0

    try:
        with open("students.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                total += int(row[1])
                count += 1

        if count > 0:
            print("Average Marks:", total / count)
        else:
            print("No data")

    except:
        print("No file found")

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Average Marks")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        average_marks()
    elif choice == "4":
        break
    else:
        print("Invalid choice")