# #1 printing this funtion with print 5
# def number_of_food_groups():
#     return 5
# print(number_of_food_groups())


#2 this will come back as an error because number_of_days_in_a_week_silicon_or_triangle_sides is not defined and can not be added to the other function
# def number_of_military_branches():
#     return 5
# print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())


#3 this will return 5 and nothing else because it only runs once and never has a reason to return any future value
# def number_of_books_on_hold():
#     return 5
#     return 10
# print(number_of_books_on_hold())


# #4 this will return 5 and print 5 and nothing else becuase the print(10) line is never called on
# def number_of_fingers():
#     return 5
#     print(10)
# print(number_of_fingers())


# #5 i dont think a variable can equal a function so an error will happen
# def number_of_great_lakes():
#     print(5)
# x = number_of_great_lakes()
# print(x)


# #6 this will print 8. 1+2 + 2+3
# def add(b,c):
#     print(b+c)
# print(add(1,2) + add(2,3))


#7 this will print 2 5 as a string
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))


#8 prints 100 then returns 10
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())


#9 returns 7 returns 14 returns 21
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))


#10 prints 8
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))


#11 prints 500 prints 500 pritns 300 prints 500
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)


#12 print 500 print 500 print 300 return 300 print 500
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)


#13 print 500 print 500 error or nothing happens print 500
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)


#14 print 1 print 3 print 2
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()


#15 not sure, maybe an error
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)