prices = [7, 1, 5, 3, 6, 4]
a = []

for i in range(len(prices)):
    for j in range(i + 1, len(prices)):
        a.append(prices[j] - prices[i])

print(a)

highest_profit = a[0]  

for p in a:
    if p > highest_profit:
        highest_profit = p

print("The highest profit is:", highest_profit)
