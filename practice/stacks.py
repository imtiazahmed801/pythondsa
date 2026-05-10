## stacks can hold many elements and the last element added is the first one to be removed e.g. stacks of pancakes
## follows LIFO principle; Last In First Out 
# basic operations:
#   Push - .append, Pop - removes and returns top element, Peek - returns top element, isEmpty, Size

trifle_layers = ["cake", "custard", "fruit", "whipped cream", "fish fingers"]
print(trifle_layers)

# peek
topElement = trifle_layers[-1]
print(topElement)

# pop 
poppedElement = trifle_layers.pop()
print(poppedElement)

print(trifle_layers)

# isEmpty
isEmpty = not bool(trifle_layers)
print(isEmpty)

# size
print(len(trifle_layers))

print(trifle_layers[-1])

print(trifle_layers)