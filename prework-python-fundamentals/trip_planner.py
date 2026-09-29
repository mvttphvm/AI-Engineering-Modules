destination_text = input("What is your destination? ")
total_distance_text = input("What is the total distance of your trip? ")
total_distance = float(total_distance_text)
car_fuel_efficiency_text = input("What is your car's fuel efficiency (miles per gallon)? ")
car_fuel_efficiency = float(car_fuel_efficiency_text)
current_gas_price_per_gallon_text = input("What is the current gas price per gallon? ")
current_gas_price_per_gallon = float(current_gas_price_per_gallon_text)
number_of_nights_stayed_text = input("How many nights will you be staying at your destination? ")
number_of_nights_stayed = int(number_of_nights_stayed_text)
average_hotel_cost_per_night_text = input("What is the average hotel cost per night? ")
average_hotel_cost_per_night = float(average_hotel_cost_per_night_text)
daily_food_budget_text = input("What is your daily food budget? ")
daily_food_budget = float(daily_food_budget_text)

gallons_of_gas_needed = total_distance / car_fuel_efficiency
total_gas_cost = gallons_of_gas_needed * current_gas_price_per_gallon
total_hotel_cost = number_of_nights_stayed * average_hotel_cost_per_night
total_food_cost = (number_of_nights_stayed+1) * daily_food_budget
grand_total_cost = total_gas_cost + total_hotel_cost + total_food_cost

print("=== Road Trip Budget Planner ===")
print(f"\nDestination: {destination_text}")
print(f"Distance: {total_distance:.2f} miles")

print("\n--- Cost Breakdown ---")
print(f"{f'Gas. ({gallons_of_gas_needed:.2f} gal @ ${current_gas_price_per_gallon:.2f}/gal):':<25}{f'${total_gas_cost:.2F}':>10}") 
print(f"{f'Hotel. ({number_of_nights_stayed} nights @ ${average_hotel_cost_per_night:.2f}/night):':<25}{f'${total_hotel_cost:.2F}':>10}")
print(f"{f'Food. ({number_of_nights_stayed+1} days @ ${daily_food_budget:.2f}/day):':<25}{f'${total_food_cost:.2F}':>10}")
print("-" * 30)
print(f"{f'Estimated Total:':<25}{f'${grand_total_cost:.2F}':>10}")

