def dis(price, discount):
    discount = 100 - discount
    discount /= 100
    price *= discount
    return price
#print(dis(10, 60))

dis=lambda p,d:p*(100-d)/100
print(dis(10, 60))