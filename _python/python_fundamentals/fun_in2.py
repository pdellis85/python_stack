# 1. Update Values in Dictionaries and Lists
x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]

# Change the value 10 in x to 15. Once you're done, x should now be[[5, 2, 3], [15, 8, 9]].
x[1][0] = 15
print(x)

# Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = 'Bryant'
print(students)

# In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

# Change the value 20 in z to 30
z[0]['y'] = 30
print(z)

# 2. Iterate Through a List of Dictionaries

students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterate_dictionary(some_list):
    for curr_dict in some_list:
        display_str = ''
        for curr_key in curr_dict.keys():
            display_str += f"{curr_key} - {curr_dict[curr_key]}, "
        # remove comma and extra space from display_str
        display_str = display_str[:len(display_str) - 2]
        print(display_str)


iterate_dictionary(students)

# 3 Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:


def iterate_dictionary2(key, some_list):
    for curr_dict in some_list:
        print(curr_dict[key])


iterate_dictionary2('first_name', students)
iterate_dictionary2('last_name', students)

# 4 Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

print(dojo)


def print_info(some_dict):
    for key in some_dict.keys():
        print(f"{len(some_dict[key])} {key.upper()}")
        for item in some_dict[key]:
            print(item)

        print('\n')


print_info(dojo)