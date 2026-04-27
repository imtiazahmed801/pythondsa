# a queue is a linear data structure that follows LIFO principle 
# basic operations 
#   enqueue, dequeue, peek, isEmpty, size

shopping_belt = ["chicken", "milk", "oranges", "dr pepper", "ice cream"]

# enqueue
shopping_belt.append("mushrooms")
shopping_belt.append("pasta")

print(shopping_belt)

# peek
frontElement = shopping_belt[0]
print('first item is', frontElement)

# dequeue 
poppedElement = shopping_belt.pop(3)
print('the first item to be scanned is', poppedElement)

# size 
print('number of items on the belt is', len(shopping_belt))

print('item first packed away is', shopping_belt[-3])