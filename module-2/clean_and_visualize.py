"""
Exercise: Clean and Visualize
Module 2 — Advanced Python & Data Handling
Estimated time: 45 minutes

Objective: Clean a messy DataFrame using pandas, then create and save
at least 2 charts using matplotlib.
"""

import os
import pandas as pd
import matplotlib

matplotlib.use("Agg")  # saves to file without needing a display
import matplotlib.pyplot as plt

# ============================================================
# Input data — do not modify this
# ============================================================

messy = pd.DataFrame(
    {
        "product": [
            "Widget A",
            "Widget B",
            "widget a",
            "Widget C",
            "Widget B",
            "Widget A",
            " Widget C",
            "Widget D",
            None,
            "Widget A",
        ],
        "sales": ["150", "200", "175", "300", "200", "180", "250", "abc", "100", "-50"],
        "date": [
            "2025-01-01",
            "2025-01-01",
            "2025-01-02",
            "2025-01-02",
            "2025-01-03",
            "2025-01-03",
            "2025-01-04",
            "2025-01-04",
            "2025-01-05",
            "2025-01-05",
        ],
        "region": [
            "North",
            "South",
            "north",
            "East",
            "South",
            "West",
            "east",
            "North",
            "South",
            "West",
        ],
    }
)

print("=" * 60)
print("BEFORE CLEANING")
print("=" * 60)
print(f"Shape: {messy.shape}")
print(messy.to_string(index=False))


# ============================================================
# TASK 1 — CLEAN the data
# Work on a copy so the original `messy` is preserved.
# ============================================================

df = messy.copy()

# TODO Step 1: Drop rows where product is null/None.
#   df = df.dropna(subset=["product"])
df = df.dropna(subset=["product"])

# TODO Step 2: Standardize product names — strip whitespace, then title case.
#   df["product"] = df["product"].str.strip().str.title()
df["product"] = df["product"].str.strip().str.title()

# TODO Step 3: Standardize region — title case is enough.
#   df["region"] = df["region"].str.strip().str.title()
df["region"] = df["region"].str.strip().str.title()

# TODO Step 4: Convert sales to numeric. Non-numeric strings become NaN.
#   df["sales"] = pd.to_numeric(df["sales"], errors="coerce")
#   df = df.dropna(subset=["sales"])   # drop rows that couldn't be converted
df["sales"] = pd.to_numeric(df["sales"], errors="coerce")
df = df.dropna(subset=["sales"])

# TODO Step 5: Remove rows where sales < 0 (negative values are data errors).
#   df = df[df["sales"] >= 0]
df = df[df["sales"] >= 0]

# TODO Step 6: Drop duplicate rows (same product, same sales, same date, same region).
#   df = df.drop_duplicates()
df = df.drop_duplicates()

# TODO Step 7: Parse the date column to datetime type.
#   df["date"] = pd.to_datetime(df["date"])
df["date"] = pd.to_datetime(df["date"])

print("\n" + "=" * 60)
print("AFTER CLEANING")
print("=" * 60)
# TODO: print shape and the cleaned df
print(f"Shape: {df.shape}")
print(df.to_string(index=False))


# ============================================================
# TASK 2 — ANALYZE & VISUALIZE
# Create at least 2 charts using plt.subplots().
# ============================================================

# TODO: compute total sales by product and daily sales totals, e.g.:
#   total_by_product = df.groupby("product")["sales"].sum().sort_values(ascending=False)
#   daily_sales      = df.groupby("date")["sales"].sum()
total_by_product = df.groupby("product")["sales"].sum().sort_values(ascending=False)
daily_sales = df.groupby("date")["sales"].sum()

# TODO: create a figure with subplots, e.g.:
#   fig, axes = plt.subplots(1, 3, figsize=(15, 5))
#   fig.suptitle("Widget Sales Analysis", fontsize=14, fontweight="bold")
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
fig.suptitle("Widget Sales Analysis", fontsize=14, fontweight="bold")

# Chart 1: Bar chart — total sales by product
# TODO: axes[0].bar(...)
axes[0].bar(total_by_product.index, total_by_product.values)

# Chart 2: Line chart — daily sales trend
# TODO: axes[1].plot(...)
axes[1].plot(daily_sales.index, daily_sales.values)

# Chart 3 (Bonus): Histogram — sales distribution
# TODO: axes[2].hist(df["sales"], ...)
axes[2].hist(df["sales"])

# TODO: plt.tight_layout()
plt.tight_layout()


# ============================================================
# TASK 3 — SAVE the chart
# ============================================================

output_dir = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "charts.png")

# TODO: plt.savefig(output_path, dpi=120, bbox_inches="tight")
# TODO: plt.close()
# TODO: print(f"Charts saved to: {output_path}")
plt.savefig(output_path, dpi=120, bbox_inches="tight")
plt.close()
print(f"Charts saved to: {output_path}")
