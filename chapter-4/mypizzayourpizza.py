pizzas = ['pepperoni', 'margherita', 'buffalo chicken']
friend_pizzas = pizzas[:]  # Create a copy using slicing

pizzas.append('hawaiian')
friend_pizzas.append('tandoori paneer pizza')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
