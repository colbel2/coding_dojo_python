x = [ [5,2,3], [10,8,9] ] # this is a list with values stored in x
students = [    #this is a dictionary containing students first and last name 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = { #this is a dictionary containing basketball players list name and socer list names
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ] 

x[1][0]=15 #changes the 10 in x to 15 and prints below
print(x) 

students[0]['last_name'] = 'Bryant'
print(f"student 1's new information is {students[0]}") #new student information is printed as byrant after being changed on line 15


sports_directory['soccer'][0] = 'Andres' #changes messi to andres in the sports_dictionary list under soccer index 0 which is the first spot
print("sports_directory was ['Messi', 'Ronaldo', 'Rooney'] ")
print('now has changed to')
for i in range(len(sports_directory['soccer'])):
    print(f"{sports_directory['soccer'][i]}")

z[0]['y'] = 30 #changes y value from 20 to 30
print(z)



students2 = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}]


def iterateDictionarycopy(anyList):
    stringReturn = ''
    for val in anyList:
        stringReturn += f"first_name - {val['first_name']}, last_name - {val['last_name']}\n"
    return stringReturn
print(iterateDictionarycopy(students2)) #prints first name last name for each student

def iterateDictionary2(key_name, some_list):
    stringReturn = ''
    for val in some_list:
        stringReturn += f"{val[key_name]} \n"
    return stringReturn
print(iterateDictionary2('first_name',students2)) #prints a list of student first names
print(iterateDictionary2('last_name',students2)) #prints a list of student last names


dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(my_dictonary): 
    for key in my_dictonary: 
        print(f"{len(my_dictonary[key])} {key.upper()}")
        for val in my_dictonary[key]:
            print(val)
        print("")
printInfo(dojo)