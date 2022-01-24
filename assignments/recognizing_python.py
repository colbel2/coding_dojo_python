# variable declaration
num1 = 42 #number
num2 = 2.3  #number
boolean = True  #boolean
string = 'Hello World' #string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #list with strings
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # list with strings, number and boolean
fruit = ('blueberry', 'strawberry', 'banana') #strings

#log statement
print(type(fruit))
print(pizza_toppings[1])
pizza_toppings.append('Mushrooms')
print(person['name'])
person['name'] = 'George'
person['eye_color'] = 'blue'
print(fruit[2])

#type check
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

#length check
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5):  #for loop start
    print(x) #for loop break
for x in range(2,5):    #for loop
    print(x)   #for loop break
for x in range(2,10,3): #for loop
    print(x)    
x = 0
while(x < 5):   #while loop
    print(x)
    x += 1

pizza_toppings.pop()
pizza_toppings.pop(1)

print(person)
person.pop('eye_color')
print(person)

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement') #single line comment
    if topping == 'Olives':
        break

def print_hello_ten_times():       #function parameter
    for num in range(10):       #function argument
        print('Hello')      #function return

print_hello_ten_times()

def print_hello_x_times(x): #function parameter
    for num in range(x):    #function argument
        print('Hello')  #function return

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)