
price_list = [900, 700, 600, 800]
discounted_price_list = []

for x in price_list:
    discounted_price = x - (x*(5/100))
    discounted_price_list.append(discounted_price)

print(discounted_price_list)

discounted_price_list = [x - (x*(5/100)) for x in price_list]
print(discounted_price_list)