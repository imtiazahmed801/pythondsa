# a data structure that is designed to be fast to work with 
# hash tables elementes stored in buckets
# hash function takes the key of an element to generate hash code
# collisions happen when elements have the same hash code and live in the same bucket
# collisions can be solved by chaining which can allow lists to allow more than one element in the same bucket

# example of hash table:

my_list = [None, None, None, None, None, None, None, None, None, None]

def hash_function(value):
    sum_of_chars = 0
    for char in value:
        sum_of_chars += ord(char)

    return sum_of_chars % 10

print("'Bob' has hash code:", hash_function('Bob'))

# unicode number = unique number that exists for every character e.g A = 65 
# modulo operator = operation that divides a number with another number and gives us the resulting remainder, written as %

def add(name):
    index = hash_function(name)
    my_list[index] = name

add('Bob')
# print(my_list)

add('Jim')
add('Steph')
add('Ella')
add('Hamza')
add('Imtiaz')

print(my_list)

def contains(name):
    index = hash_function(name)
    return my_list[index] == name

print("'Imtiaz' is in the hash table:", contains('Imtiaz'))