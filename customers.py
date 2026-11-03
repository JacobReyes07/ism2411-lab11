# Self Reflection 1
# In exercise 3, I would use .get() for finding one specific error and would use bracket notation to see any other ones that might have appeared.

# Self Reflection 2
# In exercise 8, the pattern reminds me of the columns and rows in excel and I think that python
# would be useful for identifying what group a number in excel fits into and then adding or subtracting the numbers
# in that group to get another number. This would be very fast for large data sets where individually going through
# each of them would take a lot of time.

print("--- Exercise 1 ---")

customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 12400,
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)

print("--- Exercise 2 ---")

customer["phone"] = "555-5555"
print(customer)
customer["tier"] = "platinum"
print(customer)
del customer["email"]
print(customer)

print(customer.get("ytd_spend", 0))

print("--- Exercise 3 ---")
print(customer.get("email", "no email on file"))

try:
    print(customer["email"])
except KeyError as error:
    print("KeyError caught: ", error)

print("--- Exercise 4 ---")

for key, value in customer.items():
    print(f"{key}: {value}")

for something in customer:
    print(something, customer[something])

# The second one is missing the colon and is also a little less intuitive.

print("--- Exercise 5 ---")
tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.1,
    "platinum": 0.15
}

purchase = 200
discount_rate = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1 - discount_rate)
print(f"Tier: {customer['tier']}")
print(f"Discount Rate: {discount_rate * 100}%")
print(f"Final Price: {final_price:.2f}")

print("--- Exercise 6 ---")
customers = [
    {"name": "Bob", "tier": "silver", "ytd_spend": 3200},
    {"name": "Carol", "tier": "gold", "ytd_spend": 8750},
    {"name": "David", "tier": "bronze", "ytd_spend": 450},
]

for record in customers:
    rate = tier_discounts.get(record["tier"], 0)
    discount = 300 * rate
    print(f"{record["name"]} ({record["tier"]}): ${discount:.2f} off a $300 purchase.")

print("--- Exercise 7 ---")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}

for product_name, product_details in catalog.items():
    if product_details["stock"] < 20:
        print(f"LOW STOCK: {product_name} - only {product_details["stock"]} left")

print("--- Exercise 8 ---")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200} 
]
S = 0
N = 0
for sale in transactions:
    if sale["region"] == "North":
        N += sale["amount"]
    else:
        S += sale["amount"]
print(f"South: {S}, North: {N}")

sales_by_region = {}
for sale in transactions:
    region = sale["region"]
    amount = sale["amount"]
    sales_by_region[region] = sales_by_region.get(region, 0) + amount

for region in sorted(sales_by_region):
    print(f"{region}: ${sales_by_region[region]:.2f}")