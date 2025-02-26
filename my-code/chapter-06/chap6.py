# my_person = {
#     "name": "Mieke",
#     "age": 19,
#     "language": "English"
# }

# print(my_person)

# my_person["gender"] = "female"

# print(my_person)

# my_person["age"] = "20"

# print(my_person["language"])

# del my_person["name"]

# print(my_person)

# my_person.pop("gender")

# print(my_person)

# my_numbers = {
#     "one": 1,
#     "two": 2,
#     "three": 3
# }

# print(my_numbers.get("four"))

dad = {
    "name": "Larno",
    "age": 50,
    "hometown": "Kempton",
    "hobbies": ["hunting", "guns"]
}

mom = {
    "name": "Tanja",
    "age": 51,
    "hometown": "Kempton",
    "hobbies": ["candle-making", "gardening"]
}

sibling = {
    "name": "Estee",
    "age": 25,
    "hometown": "Kempton",
    "hobbies": ["dogs", "gym"]
}

family = [dad, mom, sibling]

best_friend = {
    "name": "Cayleigh",
    "age": 19,
    "hometown": "Kempton",
    "hobbies": ["gaming", "animals"]
}

family.append(best_friend)

print(family[3]["hobbies"][0])



