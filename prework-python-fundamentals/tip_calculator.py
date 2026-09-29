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
