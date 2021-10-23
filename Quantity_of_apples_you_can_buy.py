cash= int(input("Amount of Money you have?: "))
apple_price= int(input("How much does an apple cost?: "))

ability_to_buy= cash/apple_price
change_to_an_apple= cash%apple_price

print(f"You can buy {ability_to_buy} apples and your change is {change_to_an_apple} pesos.")