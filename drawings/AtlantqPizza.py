number_of_pizzas = int(input('你想要多少个披萨？'))
cost_per_pizza = float(input('每个披萨多少钱？'))
subtotal = number_of_pizzas * cost_per_pizza
tax_rate = 0.08
sales_tax = subtotal * tax_rate
total = subtotal + sales_tax

print("总的费用是", total)
print("这里包含了", subtotal, "的披萨和", sales_tax, "的税金")
