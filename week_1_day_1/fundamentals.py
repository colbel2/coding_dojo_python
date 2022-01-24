likes_bbq = True
likes_fruit = True
weight = 110.5
iq = 300
name = "Dave"
age = "15"

if likes_bbq:
    weight += 10
    print(name + " weights " + str(weight) + "lbs")


if likes_fruit:
    weight -= 10
    print(f"{name}y weights {weight} is {age} years old and has an iq or {iq}") #uses an f string to concatate instead of + + +

if likes_bbq and weight < 100:
    weight += 10
    print (weight)
elif likes_fruit or iq > 80:
    weight -= 10
    print(weight)
    # pass is used if you dont need the elif at the time
else:
    print(weight)



question = "Why did the chicken go to the seance?"
punchline = "To get to the other side"
print(question + " | " + punchline)

# comment
#cntrl slash auto comments
'''
this is a multi-line comment
'''

ironman = {
    "name":"Tony Stark",
    "bday":"5/29/1970",
    "weight":160
}

print(ironman["name"])
ironman["age"] = 51
print(ironman)
#print(ironman.name)