#def addition(n):
 #   return n+n
#numbers = (1,2,3,4)
#result = map(addition, numbers)
#print(list(result))

my_dict = {'a': 1, 'b': 2, 'c': 3}

# Define a function to apply
def my_function(x):
    return x * 2

# Use map and dict.values()
result = tuple(map(my_function, my_dict.values()))

print(result)

