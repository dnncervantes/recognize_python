num1 = 42 # variable declaration Numbers
num2 = 2.3 # variable declaration Numbers float
boolean = True # primitive Boolean
string = 'Hello World' # primitive string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #Dictionaries
fruit = ('blueberry', 'strawberry', 'banana') # composite, Tuples
print(type(fruit)) #common function
print(pizza_toppings[1]) #lists
pizza_toppings.append('Mushrooms')#lists
print(person['name'])#lists
person['name'] = 'George'#lists
person['eye_color'] = 'blue'#lists
print(fruit[2])

if num1 > 45: #conditional if statement, 
    print("It's greater")
else: #conditional else statement
    print("It's lower") 

if len(string) < 5:#conditional if statement, length check
    print("It's a short word!")
elif len(string) > 15:#conditional else if statement, length check
    print("It's a long word!")
else:# conditional else
    print("Just right!")

for x in range(5):#for loop
    print(x)
for x in range(2,5):#for loop
    print(x)
for x in range(2,10,3):#for loop
    print(x)
x = 0
while(x < 5): #while
    print(x)
    x += 1

pizza_toppings.pop() #delete value, list
pizza_toppings.pop(1)#dleete 1 value, list

print(person)
person.pop('eye_color')#false no eye_color
print(person)

for topping in pizza_toppings: #for loop
    if topping == 'Pepperoni':#conditional if
        continue #continue
    print('After 1st if statement')
    if topping == 'Olives':#conditional if
        break #stop/break

def print_hello_ten_times():#function
    for num in range(10):#for loop
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):#function with perameter of x
    for num in range(x):#for loop
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):#function with argument
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