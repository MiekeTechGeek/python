my_likes = ["horseriding", "animals", "code", "chinchillas"]
tester = True
things = ["book", "shirt", "cup"]

for like in my_likes:
    if like == "code":
        print("Code is great")
    else:
        print("That is also cool I guess.")

if tester == True:
    print("The value is true")
else:
    print("the value is false")

if False != True:
    print("True")
else:
    print("False")

# if False == False and False == tester:
#     print("All conditions are met")
# else:
#     print("Conditions are not 100%")

# if "cup" not in things:
#     print("That is in there")

# else:
#     print("That is not in there")

# for value in my_likes:
#     if "horseriding" and "animals":
#         print("That is an odd combo")

requested_toppings = ["ham", "bacon"]

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

