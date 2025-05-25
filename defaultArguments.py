import time

def count(end, start=0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("Done!")

# count(10)

# Key arguments
def greeting(greeting, title, name):
    print(f"{greeting}, {title} {name}!")

#greeting("Hello", name="Sabrina", title="Ms.")

def sumNumbers(*args):
    total =0 
    for arg in args:
               total += arg
    print(f"Total: {total}")

# sumNumbers(10,20,30,40)

def mountAdress(**kwargs):
    # for value in kwargs.values():
    #     print(value, end=" ")
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")

    print(f"Only street name: {kwargs.get("street")}")

mountAdress(street="Fake St.", city="San Francisco", state="California", zip="45637")