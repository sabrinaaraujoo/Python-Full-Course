# LEGB - local, enclosed, global, built in

from math import e

# build in
print(e)

e = 7

print(e)

def printX():
    # local
    x = 10
    print(x)

    def printYandX():
        y = 2
        print(f"{x} enclosed")
        print(f"{y} local")
        print(f"{z} Global")
        
    printYandX()
    
z = 20 # Global
printX()


