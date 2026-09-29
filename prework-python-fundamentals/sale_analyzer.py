import csv

widget_sales = []

with open("sales_data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        #converting int and floats to store in list
        row["quantity"] = int(row["quantity"])
        row["price"] = float(row["price"])
        widget_sales.append(row)


def calculator(sold_widgets):
    total_revenue = 0
    product_revenue = {}
    product_quantity = {}
    daily_revenue = {}

    for row in sold_widgets:
        #calculate revenue for this sale
        revenue = row ["quantity"] * row["price"]

        #adding to total revenue
        total_revenue += revenue

        product = row["product"]
        date = row["date"]

        if product not in product_revenue:
            product_revenue[product] = 0

        product_revenue[product] += revenue

        #add quantity to the product total
        if product not in product_quantity:
            product_quantity[product] = 0

        product_quantity[product] += row["quantity"]

        #add revenue to the daily total
        if date not in daily_revenue:
            daily_revenue[date] = 0

        daily_revenue[date] += revenue
    highest_revenue_day = max(daily_revenue, key=daily_revenue.get)

    return total_revenue, product_revenue, product_quantity, daily_revenue, highest_revenue_day


# Call the function to get these values
total_revenue, product_revenue, product_quantity, daily_revenue, highest_revenue_day = calculator(widget_sales)


# Write the text report
with open ("sales_report.txt", "w") as file:
    file.write("--- Sales Report ---\n")
    file.write(f"Total revenue: ${total_revenue:.2f}\n")
    file.write(f"Highest revenue day: {highest_revenue_day}\n")
    file.write(f"Revenue on highest day: ${daily_revenue[highest_revenue_day]:.2f}\n\n")

    file.write("Revenue per product:\n")

    for product in product_revenue:
        file.write(f"{product}: ${product_revenue[product]:.2f}\n")


# Write the product summary CSV
with open("product_summary.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["product", "total_quantity", "total_revenue"])

    for product in product_revenue:
        writer.writerow([
            product,
            product_quantity[product],
            f"{product_revenue[product]:.2f}"
        ])

