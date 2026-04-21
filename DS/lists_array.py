## Lists are built in data structures that serves as a dynamic array 
## Lists are orederd, mutable and can contain multiple elements and used by many algorithms 

## example of a list of integers
pirate_crew = [1, 2, 3, 4]

# list of mixed types
straw_hats = ["luffy", "zoro", 3, True]

print(pirate_crew)
print(straw_hats)

## List methods - perform common operations like appending, sorting, etc 
world_gov = ["sengoku", "garp", "koby"]
world_gov.append("aoikiji")
print(world_gov)

world_gov.sort()

five_elder_stars = [1, 3, 2, 4]
five_elder_stars.append(5)
five_elder_stars.sort()

print(five_elder_stars)

## creating algorithims - alg to find the lowest value 
my_numbers = [56, 33, 28, 8, 2, 10]
minVal = my_numbers[0]

for i in my_numbers:
    if i < minVal:
        minVal = i 

print('Lowest value is', minVal)

op_locations = ["elbaph", "wano", "water 7"]
op_locations.append("enies lobby")
op_locations.sort()

print(op_locations)