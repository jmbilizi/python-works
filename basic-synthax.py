# console.log in py
print('Hello World')

# variable definition in py
my_name: str = 'Janvier'
print('My name is ' + my_name)

# function declaration in py
def mySumFun(a: int, b: int) -> int:
    sum = a + b
    return sum

print(mySumFun(12, 26))

def my_function(*kids):
  print("The youngest child is " + kids[2]) #If the number of arguments is unknown, add a * before the parameter name:
my_function("Emil", "Tobias", "Linus")

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus") #You can also send arguments with the key = value syntax. This way the order of the arguments does not matter.

# Loops in py
fruits = ["apple", "banana", "cherry"]

for x in fruits:
  print(x)

for x in "banana":
  print(x)

for x in fruits:
  print(x)
  if x == "banana":
    break
  
for x in fruits:
  if x == "banana":
    continue
  print(x)

for x in range(0, 10, 3):
    print(x)