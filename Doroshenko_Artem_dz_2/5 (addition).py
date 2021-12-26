import random

amount = random.randint(10, 20)
items = []
for i in range(0, amount - 1):
    price = round(random.uniform(0, 200), 2)
    items.append(price)
print(items)

