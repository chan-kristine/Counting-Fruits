print("The price of Apple is 20 pesos")
print("The price of Orange is 25 pesos")

apple_price= 20
orange_price= 25

quantity_of_oranges_you_want_to_buy = int(input("How many oranges you want to buy?: "))
quantity_of_apples_you_want_to_buy = int(input("HOw many apples you want to buy?: "))

sum_of_oranges = orange_price * quantity_of_oranges_you_want_to_buy
sum_of_apples = apple_price * quantity_of_apples_you_want_to_buy
amount= sum_of_oranges + sum_of_apples

print(f"The total amount is: {amount}.")