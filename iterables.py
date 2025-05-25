# Iterables = An object/collection that can return its element one at a time,
#             allowing it to be interated over in a loop


## List
numbers = [1, 2, 3, 4, 5]

for number in reversed(numbers):
    print(number, end=" ")
print()

## Tuples
letters = ("A", "B", "C", "D", "E")

for letter in reversed(letters):
    print(letter, end= " ")
print()

## Set
fruits = {"orange", "banana", "apple", "Blueberry"}

for fruit in fruits: # reversed doesn't work
    print(fruit, end=" ")
print()

## Dictionary
users = {"id": 132, "name": "Sabrina", "age": 23}

for user in users:
    print(user, end=" ") 
print()

for user in users.values():
    print(user, end=" ") 
print()

for key, user in users.items():
    print(f"{key}: {user}", end=" ") 
print()

## String
word = "Sabrina"

for letter in word:
    print(letter.upper(), end=" ")