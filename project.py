#shopping cart program
foods=[]
prices=[]
total=[]
total=0

while True:
    food =input("Enter a food to buy (q to quit):")
    if food.lower()=="q":
        break
    else:
        price= float(input(f"Entre the price of a {food}:$"))
        foods.append(food)
        prices.append(price)   
print("--------YOUR CART---------")     
for food in foods:
    print(food,end="" )     
for price in prices:
    total+= price   
print(f"Your total is :${total}")        
        