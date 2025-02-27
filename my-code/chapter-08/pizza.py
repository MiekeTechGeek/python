def pizza_oven(*toppings):
    print(f"Here is your {toppings} pizza.")

pizza_oven("Ham", "Cheese", "Pepper")

def pizza_fail(customer):
    print(f"{customer}'s pizza has been burnt.")

# def test(*first, second):
#     print(f"these are my first arguments: {first}")
#     print(f"this is my other argument: {second}")

# test(1, 2, 3, 4, second = 5)