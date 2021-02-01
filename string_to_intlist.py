# lambda function

a = [1, 2, 3, 4]
# inline function as variable
x = lambda i: a[i]
print(x(2))

# lets say i want to increase each number in list by 1
def increase(i):
    return i+1

a = map(increase, a)
print(a)

# small functions can be written as lambda functions as well
a = map(lambda i: i+1, a)
print(a)

#now we are taking spaceseperated numbers as input and converting it to array in one line
a = map(lambda i: int(i), raw_input("Enter space seperated numbers ").split())
print(a)

# lambda function with two inputs
fruits = map(lambda i,j: i+j, ("app","ora","ban","jack","mel"), ("le","nge", "ana","fruit", "on"))
print(fruits)