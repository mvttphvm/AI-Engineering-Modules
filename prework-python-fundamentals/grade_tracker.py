import csv


def load_students(filepath):
    try:
        with open(filepath) as file:
            reader = csv.DictReader(file)
            students = list(reader)

        return students

    except FileNotFoundError:
        print("File not found.")
        return []


def calculate_average(grades):
    valid_grades = []

    for grade in grades.values():

        if grade == "":
            continue

        try:
            grade = float(grade)
        except ValueError:
            continue

        if 0 <= grade <= 100:
            valid_grades.append(grade)

    if not valid_grades:
        return None

    return round(sum(valid_grades) / len(valid_grades), 1)


def get_letter_grade(average):
    if average is None:
        return "N/A"
    elif average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def generate_report(students):

    total_number_of_students = len(students)

    # Keep each student's average so we can get the class average later.
    class_average = []

    highest_student_average = None

    lowest_student_average = None

    grade_distribution = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "F": 0,
        "N/A": 0
    }

    indivudal_students_results = []

    for student in students:

        average = calculate_average(student)

        if average is not None:
            class_average.append(average)

            # Set the first valid average as both the highest and lowest.
            if highest_student_average is None or average > highest_student_average:
                highest_student_average = average

            if lowest_student_average is None or average < lowest_student_average:
                lowest_student_average = average

        letter_grade = get_letter_grade(average)

        grade_distribution[letter_grade] += 1

        student_result = {
            "Student name": student["student_name"],
            "Numeric average": average,
            "Letter grade": letter_grade
        }

        indivudal_students_results.append(student_result)

    # Calculate the class average from the student averages.
    if class_average:
        class_average = round(sum(class_average) / len(class_average), 1)
    else:
        class_average = None

    report = {
        "total_students": total_number_of_students,
        "class_average": class_average,
        "highest_average": highest_student_average,
        "lowest_average": lowest_student_average,
        "grade_distribution": grade_distribution,
        "individual_results": indivudal_students_results
    }

    return report


def write_report(report, filepath):
    with open(filepath, "w") as file:

        file.write("STUDENT GRADE REPORT\n")
        file.write("=" * 35 + "\n\n")

        file.write("Class Summary\n")
        file.write("-" * 35 + "\n")
        file.write(f"Total students: {report['total_students']}\n")
        file.write(f"Class average: {report['class_average']}\n")
        file.write(f"Highest average: {report['highest_average']}\n")
        file.write(f"Lowest average: {report['lowest_average']}\n\n")

        file.write("Grade Distribution\n")
        file.write("-" * 35 + "\n")

        for grade, count in report["grade_distribution"].items():
            file.write(f"{grade}: {count}\n")

        file.write("\n")

        file.write("Individual Student Results\n")
        file.write("-" * 35 + "\n")

        for student in report["individual_results"]:
            file.write(
                f"{student['Student name']}: "
                f"{student['Numeric average']} "
                f"({student['Letter grade']})\n"
            )


def main():
    print("Loading student data...")

    students = load_students("data/students.csv")

    print(f"  Loaded {len(students)} students.")

    print("\nGenerating report...")
    report = generate_report(students)

    print("\n--- Summary ---")
    print(f"Total students:   {report['total_students']}")
    print(f"Class average:    {report['class_average']}")
    print(f"Highest average:  {report['highest_average']}")
    print(f"Lowest average:   {report['lowest_average']}")

    print("\nGrade Distribution:")

    for grade, count in report["grade_distribution"].items():
        print(f"  {grade}: {count}")

    sorted_students = sorted(
        report["individual_results"],
        key=lambda student: (
            student["Numeric average"]
            if student["Numeric average"] is not None
            else -1
        ),
        reverse=True
    )

    print("\nTop 5 students:")

    for student in sorted_students[:5]:
        print(
            f"  {student['Student name']:<20}"
            f"{student['Numeric average']}  "
            f"({student['Letter grade']})"
        )

    write_report(report, "grade_report.txt")

    print("\nReport written to grade_report.txt")


if __name__ == "__main__":
    main()