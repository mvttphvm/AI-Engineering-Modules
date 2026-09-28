"""
Exercise: Student Score Analysis
Module 2 — Advanced Python & Data Handling
Estimated time: 35 minutes

Objective: Answer 6 questions about student data using pandas operations.
No manual for-loops — use pandas methods throughout.
"""

import pandas as pd

data = {
    "student":       ["Alice", "Bob", "Charlie", "Diana", "Eve",
                      "Frank", "Grace", "Henry", "Iris", "Jack"],
    "course":        ["Python", "Python", "SQL", "SQL", "Python",
                      "SQL", "Python", "SQL", "Python", "SQL"],
    "score":         [92, 78, 85, 91, 88, 72, 95, 68, 84, 90],
    "hours_studied": [20, 12, 18, 22, 15, 8, 25, 10, 16, 19],
    "passed":        [True, True, True, True, True, False, True, False, True, True],
}
df = pd.DataFrame(data)

print("=" * 60)
print("Raw Data")
print("=" * 60)
print(df.to_string(index=False))


# ============================================================
# Q1 — How many students are in each course?
# Hint: df["column"].value_counts() counts occurrences of each unique value.
#       Equivalent to GROUP BY COUNT in SQL.
# ============================================================
print("\n" + "=" * 60)
print("Q1 — Students per course")
print("=" * 60)
# TODO: print( df["course"].value_counts() ... )
print( df["course"].value_counts().sort_index())


# ============================================================
# Q2 — What is the average score per course?
# Hint: df.groupby("col")["other_col"].mean()
#       Chain .round(1) to limit decimal places.
# ============================================================
print("\n" + "=" * 60)
print("Q2 — Average score per course")
print("=" * 60)
# TODO: avg_score = df.groupby(...)[...].mean().round(1)
#       print(avg_score.to_string())
avg_score = df.groupby("course")["score"].mean().round(1)
print(avg_score.to_string())


# ============================================================
# Q3 — Who are the top 3 students by score?
# Hint: df.nlargest(n, "column") returns the n rows with the highest values.
#       Select only the columns ["student", "course", "score"] for clean output.
# ============================================================
print("\n" + "=" * 60)
print("Q3 — Top 3 students by score")
print("=" * 60)
# TODO: top3 = df.nlargest(3, "score")[["student", "course", "score"]]
#       print(top3.to_string(index=False))
top3 = df.nlargest(3, "score")[["student", "course", "score"]]
print(top3.to_string(index=False))


# ============================================================
# Q4 — What is the average hours_studied for students who passed vs. failed?
# Hint: The "passed" column is boolean — you can groupby a boolean column.
#       After groupby, rename the index labels to "Passed"/"Failed" for clarity.
# ============================================================
print("\n" + "=" * 60)
print("Q4 — Avg hours studied: passed vs. failed")
print("=" * 60)
# TODO: avg_hours = df.groupby("passed")["hours_studied"].mean().round(1)
#       avg_hours.index = avg_hours.index.map({True: "Passed", False: "Failed"})
#       print(avg_hours.to_string())
avg_hours = df.groupby("passed")["hours_studied"].mean().round(1)
avg_hours.index = avg_hours.index.map({True: "Passed", False: "Failed"})
print(avg_hours.to_string())


# ============================================================
# Q5 — Add a "grade" column: 90+="A", 80-89="B", 70-79="C", <70="F"
# Hint: pd.cut(df["score"], bins=[...], labels=[...], right=False)
#       bins=[0, 70, 80, 90, 101] with right=False gives [0,70), [70,80), [80,90), [90,101)
#       → F, C, B, A
# ============================================================
print("\n" + "=" * 60)
print("Q5 — Add 'grade' column")
print("=" * 60)
# TODO: df["grade"] = pd.cut(df["score"], bins=..., labels=..., right=False)
#       print(df[["student", "score", "grade"]].to_string(index=False))
df["grade"] = pd.cut(df["score"], bins = [0, 70, 80, 90, 101], labels=["F", "C", "B", "A"], right=False)
print(df[["student", "score", "grade"]].to_string(index=False))


# ============================================================
# Q6 — What is the grade distribution per course?
# Hint: df.groupby("course")["grade"].value_counts().unstack(fill_value=0)
#       Then reorder columns: [["A", "B", "C", "F"]]
# ============================================================
print("\n" + "=" * 60)
print("Q6 — Grade distribution per course")
print("=" * 60)
# TODO: grade_dist = (
#           df.groupby("course")["grade"]
#           .value_counts()
#           .unstack(fill_value=0)
#           [["A", "B", "C", "F"]]
#       )
#       print(grade_dist.to_string())
grade_dist = (
                df.groupby("course")["grade"]
                .value_counts()
                .unstack(fill_value=0)
               [["A", "B", "C", "F"]]
               )
print(grade_dist.to_string())