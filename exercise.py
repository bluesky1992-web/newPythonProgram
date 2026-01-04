item = input('What item would you like to buy? ')

price = float(input('what is the price ? :'))

quantity = int(input('How many would you like?: '))

total = price * quantity

print(f'You have bought {quantity} x {item}/s')
print(f'Your total is: ${total}')
