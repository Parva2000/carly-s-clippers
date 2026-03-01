hairstyle = ["bouffant","pixie","dreadlocks","crew","bowl","bob","mohak","flattop"]

prices = [30, 25, 40, 20, 15, 10, 50, 35]
 
last_week = [2, 3, 5, 8, 4, 4, 6, 2]
total_price = 0

for price in prices :
    total_price += price
print(total_price)
average_price = total_price /len(prices)
print(average_price)
for price in prices :
    new_price = price - 5
    print(new_price)
    total_renvenue = 0
    for i in range(len(hairstyle)) :
     total_renvenue += prices[i] * last_week[i]
print(total_renvenue)