for i in range(1, 151):
    print(i)

for i in range(5,1005,5):
    print(i)

for i in range(1, 1005):
    if i == i/5:
        print("Coding")
    else:
        print(i)

def counting_dojo():
    for i in range (1,101,1):
        if i % 5 == 0:
            print ('Coding')
        if i % 10 == 0:
            print ('Dojo')

counting_dojo()

minimum = 0
maximum = 500000
Oddtotal = 0

for number in range(minimum, maximum+1):
    if(number % 2 != 0):
        print("{0}".format(number))
        Oddtotal = Oddtotal + number

print("The Sum of Odd Numbers from {0} to {1} = {2}".format(minimum, maximum, Oddtotal))

def countdown():
    number = 2018
    while number > 0:
        print (number)
        number = number - 4
        
countdown()   

