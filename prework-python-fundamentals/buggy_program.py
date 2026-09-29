# buggy_program.py — Contains 4 bugs. Find and fix them all.

def calculate_stats(numbers):
    """1) No : at the end of def a function line
    2) SyntaxError
    3)Put : at the end
    4)Found myself
    """
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    
    above_average = []
    for num in numbers:
        if num > average:
            """1) No : at the end of if statement line
            2) SyntaxError
            3)Put : at the end
            4)Found myself"""
            above_average.append(num)
    
    return {
        "total": total,
        "average": average,
        "above_average": above_average,
        "above_count": len(above_average)
    }

scores = [85, 92, 78, 95, 88, "70", 93]
"""1) "70" in the list is a string
2) TypeError in calculate stats() sum()
3)change to 70 or ensure all items in a list to int.
4)Found myself"""
result = calculate_stats(scores)

print(f"Total: {result['total']}")
print(f"Average: {result["average"]}")
"""1)average is supposed to be a string
2) NameError because the key is a string not a variable
3)put "" around average
4)Found myself"""

print(f"Above average: {result['above_count']} scores")



#pasting my tip_calculator.py here to be ran
print("=" * 35)
print("            Tip Calculator")
print("=" * 35)

bill_text = input("\nEnter the billl amount: $")
bill = float(bill_text)

tip_15 = bill * 0.15
tip_18 = bill * 0.18
tip_20 = bill * 0.20
tip_25 = bill * 0.25

total_15 = bill + tip_15
total_18 = bill + tip_18
total_20 = bill + tip_20
total_25 = bill + tip_25

people_text = input("How many people are splitting the bill? ")
people = int(people_text)

print("\nBill amount: ${:.2f}")
print(f"Number of people: {people}")
print("-" * 35)
print(f"{'Tip %':<10}{'Tip':<10}{'Total':<10}{'Per Person':<10}")
print("-" * 35)
print(f"{'15%':<10}${tip_15:<9.2f}${total_15:<9.2f}${total_15/people:<9.2f}")
print(f"{'18%':<10}${tip_18:<9.2f}${total_18:<9.2f}${total_18/people:<9.2f}")
print(f"{'20%':<10}${tip_20:<9.2f}${total_20:<9.2f}${total_20/people:<9.2f}")
print(f"{'25%':<10}${tip_25:<9.2f}${total_25:<9.2f}${total_25/people:<9.2f}")
print("=" * 35)
"""
# 1. How can I make this code more Pythonic?

Suggestion: Put the tip percentages in a list instead of making 4 separate variables.

tip_percentages = [0.15, 0.18, 0.20, 0.25]

Evaluation:
* Do I understand every line? Yes. It is a list of the 4 tip amounts.
* Does it run? Yes.
* Does it handle edge cases? No, but this change doesn't cause any new problems.
* Are the functions real? Yes. Lists are a normal Python feature.
* Does it fit my project? Yes.
* Could I explain it? Yes.

Decision: I would use it because it makes the code shorter and avoids repeating myself.

Verification: The list works correctly in Python.

---

# 2. What edge cases am I not handling?

Suggestion: Don't allow 0 people because the program would try to divide by zero.

if people == 0:
    print("Number of people must be greater than 0.")

Evaluation:

* Do I understand every line? Yes. It checks if the number of people is 0.
* Does it run? Yes.
* Does it handle an edge case? Yes. It handles 0 people.
* Are the functions real? Yes. print() is a real Python function.
* Does it fit my project? Yes.
* Could I explain it? Yes.

Decision: I would use it because dividing by 0 would crash the program.

Verification: The if statement correctly finds when people is 0.

---

# 3. Are there any security or reliability concerns?

Suggestion: Check the bill input so letters like abc don't crash the program.

try:
    bill = float(bill_text)
except ValueError:
    print("Please enter a valid bill amount.")

Evaluation:

* Do I understand every line? Yes. It tries to turn the input into a number and catches the error if it can't.
* Does it run? Yes.
* Does it handle edge cases? Yes. It handles invalid input like abc.
* Are the functions real? Yes. float() and print() are real Python functions, and try/except is built into Python.
* Does it fit my project? Yes.
* Could I explain it? Yes.

Decision: I would use it because it makes the program more reliable and stops it from crashing on bad input.

Verification: The code catches a ValueError when the bill isn't a valid number.
"""