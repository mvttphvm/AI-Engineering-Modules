print("="*3 + "Grade Analyzer" + "="*3)

# starting list of scores to analyze
scores = [88, 45, 92, 67, 73, 95, 81, 56, 78, 100, 62, 85, 90, 38, 71]

# basic stats - count, average, high, low
total_scores = len(scores)
average_score = sum(scores) / len(scores)
print(f"Total scores: {total_scores}")
print(f"Average: {average_score:.1f}")
print(f"Highest: {max(scores)}")
print(f"Lowest: {min(scores)}")

# empty lists to sort scores into by letter grade
a_scores = []
b_scores = []
c_scores = []
d_scores = []
f_scores = []

# loop through every score once and drop it into the right grade bucket
for score in scores:
    if score in range(90, 101):
        a_scores.append(score)
    elif score in range(80,90):
        b_scores.append(score)
    elif score in range(70,80):
        c_scores.append(score)
    elif score in range(60,70):
        d_scores.append(score)
    elif score <60:
        f_scores.append(score)

# passing = A/B/C/D combined, failing = just F
passing_scores = len(a_scores)+len(b_scores)+len(c_scores)+len(d_scores)
percentage_of_passing_scores = round((passing_scores/len(scores))*100,1)
failing_scores = len(f_scores)
percentage_of_failing_scores = round((failing_scores/len(scores))*100,1)
print(f"Passing: {passing_scores}  ({percentage_of_passing_scores}%)")
print(f"Failing: {failing_scores}  ({percentage_of_failing_scores}%)")

# how many landed in each letter grade
print("\nGrade Distribution:")
print(f"A: {len(a_scores)} students")
print(f"B: {len(b_scores)} students")
print(f"C: {len(c_scores)} students")
print(f"D: {len(d_scores)} students")
print(f"F: {len(f_scores)} students")

# let user keep adding scores, recalculating average each time, until they type "done"
print("\n--- Add More Scores ---")
user_input=""
while user_input.lower() !="done":
    user_input = input("Enter a score (or 'done' to finish): ")
    try:
        users_score = int(user_input)
        if 0 <= users_score <=100:
            scores.append(users_score)
            average_score = sum(scores) / len(scores)  # recalc so it's not stale
            print(f"Updated average: {average_score:.1f}")
        else:
            print("Number must be bewteen 0 and 100. Try again.")
    except ValueError:
        print("That's not a valid number. Try again.")

print(f"Final average: {average_score:.1f}")