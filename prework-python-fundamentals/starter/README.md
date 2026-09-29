"""
Student Grade Tracker

This is a Python program that reads student grades from a CSV file and creates a grade report.


What the program does:

1)Reads the student data from data/students.csv 
2)Calculates each student's average
3)Gives each student a letter grade
4)Calculates the class average, highest average, and lowest average
5)Shows the grade distribution
6)Shows the top 5 students
7)Creates a grade_report.txt file with the full report

Project Files

starter/
├── data/
│   └── students.csv
├── grade_tracker.py
├── requirements.txt
└── README.md

requirements.txt is empty because this project only uses Python's built-in csv module.
There are no external packages needed.


How to Run:

Make sure you are in the project folder (starter), then run:

grade_tracker.py

The program will read the CSV file and show the results in the terminal.

It will also create:

grade_report.txt

The report file has the class summary, grade distribution, and individual student results.

Example Output:

--- Summary ---
Total students:   15
Class average:    79.4
Highest average:  95.2
Lowest average:   58.2


The results can change depending on the data in students.csv.
"""
