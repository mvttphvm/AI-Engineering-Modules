def calculate_average(list_of_numbers):
    """Takes a list of numbers, returns the average. Returns 0 if the list is empty."""
    # Check if the list is empty so we don't divide by zero
    if not list_of_numbers:
        return 0
    else:
        average = sum(list_of_numbers)/len(list_of_numbers)
    return average


def find_max_and_min(list_of_numbers):
    """Takes a list of numbers, returns a tuple 
    (max_value, min_value) w/o using max() or min()"""

    # Start with the first number as both the highest and lowest
    highest = list_of_numbers[0]
    lowest = list_of_numbers[0]

    # Go through the list and update highest if we find a bigger number
    for number in list_of_numbers:
        if number > highest:
            highest = number

    # Go through the list again and update lowest if we find a smaller number
    for number in list_of_numbers:
        if number < lowest:
            lowest = number

    return (highest, lowest)


def count_occurrences(items_list, target_value):
    """Takes a list and a target value, returns how many times 
    the target appears in the list without using count()"""
    
    # Start the count at zero
    count = 0

    # Check each item to see if it matches the target
    for number in items_list:
        if number == target_value:
            count +=1

    return count


def is_palindrome(text):
    """Takes a string, returns True if it reads the same forward 
    and backward (case-insensitive, ignoring spaces)."""
    
    # Make everything lowercase and remove spaces
    cleaned_text = text.lower().replace(" ", "")

    # Compare the text to itself backwards
    if cleaned_text == cleaned_text[::-1]:
        return True
    else:
        return False


def create_report(title, list_of_scores):
    """Takes a report title and a list of scores. Uses calculate_average 
    and find_max_and_min internally. Returns a formatted string report"""
    
    # Get the average, highest score, and lowest score
    average = calculate_average(list_of_scores)
    highest, lowest = find_max_and_min(list_of_scores)

    # Build the report one line at a time
    report = f"--- {title} ---\n"
    report += f"Total scores: {len(list_of_scores)}\n"
    report += f"Average: {average:.1f}\n"
    report += f"Highest: {highest}\n"
    report += f"Lowest: {lowest}"

    return report


# Test Section

# Test 1
# Test each function with a normal list of scores
if __name__ == "__main__":
    test_scores = [85, 92, 78, 95, 88, 70, 93]
        
    print(f"Average: {calculate_average(test_scores)}")
    print(f"Max/Min: {find_max_and_min(test_scores)}")
    print(f"Count of 85: {count_occurrences(test_scores, 85)}")
    print(f"'racecar' palindrome: {is_palindrome('racecar')}")
    print(f"'hello' palindrome: {is_palindrome('hello')}")
    print()
    print(create_report("Class Scores", test_scores))


    # Test 2
    # Make sure an empty list returns 0 instead of causing an error
    print(f"Empty average: ", calculate_average([]))
    # Expecting a 0


    # Test 3
    # Check what happens when an empty list is passed to find_max_and_min
    try:
        print("Empty max/min:", find_max_and_min([]))
    except IndexError:
        print("Empty max/min: IndexError (empty lists are not supported)")
    # Expecting an IndexError


    # Test 4
    # Make sure count_occurrences counts the target more than once
    print("Multiple occurrences:", count_occurrences([1, 2, 2, 3, 2], 2))
    # Expecting 3


    # Test 5
    # Test a palindrome with spaces and different capitalization
    print("Palindrome with spaces/mixed case:", is_palindrome("Never Odd Or Even"))
    # Expecting True


    # Test 6
    # Test a single character
    print("Single character palindrome:", is_palindrome("A"))
    # Expecting True