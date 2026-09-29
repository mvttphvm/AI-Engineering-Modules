"""
#Part 1 - Classify Space Complexity
# Function A
def reverse_string(s):
    return s[::-1]
#O(1)Doesn't build anything that grows.

# Function B
def count_letters(text):
    counts = {}
    for char in text:
        counts[char] = counts.get(char, 0) + 1
    return counts
#O(n)because it returns the same amount as the input    

# Function C
def matrix_identity(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]
#O(n^2) since it returns a matrix nxn with 1's where i and j are the same

# Function D
def running_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    print(total)
#O(1) because regardless of the input size it always prints the total once
"""

#Part 2 - Tradeoff Decision
import csv


# Set approach
# Time Complexity: O(n) 
# Space Complexity: O(n)
def duplicates_with_set(filename):
    seen = set()
    duplicates = set()

    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            email = row["email"]

            if email in seen:
                duplicates.add(email)
            else:
                seen.add(email)

    return duplicates


# Sort-and-scan approach
# Time Complexity: O(n log n)
# Space Complexity: O(n)
def duplicates_with_sort(filename):
    emails = []

    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            emails.append(row["email"])

    emails.sort()

    duplicates = []

    for i in range(1, len(emails)):
        if emails[i] == emails[i - 1]:
            if not duplicates or duplicates[-1] != emails[i]:
                duplicates.append(emails[i])

    return duplicates

"""
On a machine with 4GB of RAM, I would choose the sort-and-scan approach. Both approaches use O(n) space, but a list generally uses less memory per item than a set. With 5 million emails and limited RAM, I would prioritize making sure I do not run out of memory, even though sorting is slower.


On a machine with 64GB of RAM, I would choose the set approach. Since I have much more memory available, I would prioritize speed. The sort-and-scan approach takes O(n log n) time because the emails have to be sorted first.
"""


