# list comprehensions = A concise way to create list in Python
#                       Compact and easier to read than tradicional loops
#                       [expression for value in iterable if condicional] 

# long list loop

double = []
for x in range(1,11):
    double.append(x * 2)

# short list loop
double2 = [x * 2 for x in range(1, 11)]

numbers_even = [x for x in range(1, 11) if x % 2 == 0]

print(numbers_even)