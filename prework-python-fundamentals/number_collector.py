# Snippet 1 - making this snippet a comment to run code 
#print("The answer is: " + 42) 
"""
(1) 42 Will raise a TypeError
(2) I was right
(3) conert 42 with str() to avoid the error
"""
# Snippet 2 - making this snippet a comment to run code 
"""
favorite = input("Favorite number: ") 
result = favorite + 10
print(result)
"""
"""
(1) Will raise a TypeError with favorite because input() always returns a string
(2) I was right
(3) convert favorite with int() to avoid the error
"""
# Snippet 3 - making this snippet a comment to run code 
#print("Hello World) 
"""
(1) Will raise a SyntaxError because of the missing closing quote
(2) I was right
(3) Add the closing quote to avoid the error
"""
# Snippet 4 - making this snippet a comment to run code 
#age = int("twenty-five")
"""
(1) Will raise a ValueError because "twenty-five" cannot be converted to an integer
(2) I was right
(3) Use a valid integer string like "25" to avoid the error
"""
# Snippet 5
#print(username)
"""
(1) Will raise a NameError because username is not defined
(2) I was right
(3) Define username before using it to avoid the error
"""



try:
    num1=int(input("Enter number 1: "))
    if num1 < 0:
        raise ValueError("Number must be non-negative")
    if not isinstance(num1, int):
        raise ValueError("Number must be a positive whole number")
except ValueError as v:
    num1=0
    print("Error occured: That's not a valid number. Using 0 instead,", v)

try:
    num2=int(input("Enter number 2: "))
    if num2 < 0:
        raise ValueError("Number must be non-negative")
    if not isinstance(num2, int):
        raise ValueError("Number must be a positive whole number")
except ValueError as v:
        num2=0
        print("Error occured: That's not a valid number. Using 0 instead,", v)


try:
    num3=int(input("Enter number 3: "))
    if num3 < 0:
        raise ValueError("Number must be non-negative")
    if not isinstance(num3, int):
        raise ValueError("Number must be a positive whole number")
except ValueError as v:
    num3=0
    print("Error occured: That's not a valid number. Using 0 instead,", v)


print(f"Your numbers are: {num1}, {num2}, {num3}")
total = num1 + num2 + num3
print(f"Sum:  {total}")
print(f"Average: {total / 3 if total > 0 else 0:.2f}")