item1_name_string = "Notebook"
item1_price_string = "4.99"
item1_qty_string = '2'

item2_name_string= "Pen Pack"
item2_price_string = "7.50"
item2_qty_string = '1'

item3_name_string = "Backpack"
item3_price_string = "34.99"
item3_qty_string = '1'

tax_rate_string = "0.075"

item1_price = float(item1_price_string)
item1_qty = int(item1_qty_string)
item2_price = float(item2_price_string)
item2_qty = int(item2_qty_string)
item3_price = float(item3_price_string)
item3_qty = int(item3_qty_string)

tax_rate = float(tax_rate_string)

notebook_total = item1_price * item1_qty
pen_pack_total = item2_price * item2_qty
backpack_total = item3_price * item3_qty

subtotal_string = "Subtotal"
subtotal = notebook_total + pen_pack_total + backpack_total
tax_string = "Tax"
tax = subtotal * tax_rate

total_string = "Total"
total = subtotal + tax

print("=" * 60)
print(" " * 20 + "STORE RECEIPT")
print("=" * 60)
print(f"{item1_name_string}  {" " * 10}  ${item1_price:.2f}  x  {item1_qty}  {" " * 8} ${notebook_total:.2f}")
print(f"{item2_name_string}  {" " * 10}  ${item2_price:.2f}  x  {item2_qty}  {" " * 8} ${pen_pack_total:.2f}")
print(f"{item3_name_string}  {" " * 10}  ${item3_price:.2f}  x  {item3_qty}  {" " * 8} ${backpack_total:.2f}")
print("-" * 60)
print(f"{subtotal_string}: {" " * 38} ${subtotal:.2f}")
print(f"tax: {" " * 43} ${tax:.2f}")
print("=" * 60)
print(f"{total_string}: {" " * 41} ${total:.2f}")
print("=" * 60)