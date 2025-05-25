foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy: (q to quit) ")
    if food == "q":
        break
    else:
        price = float(input(f"Enter the price of {food}: $"))
        foods.append(food)
        prices.append(price)
        
print("****** YOUR CART ******")
for food in foods:
    for price in prices:
        total += price
    print(food, end="")  

print()
print(f"Total: ${total:.2f}")