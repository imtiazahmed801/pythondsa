# when a function calls itself
# benefit of looping through data to reach a result 
# helps to visualise complex problems into basic steps
# problems are either solved iteratively or recursively 
# iterative = faster, complex
# recursive = slower, simpler

# simple recursion 
#def countdown(n):
#    if n <= 0:
#        print("Done!")
#    else:
#        print(n)
#        countdown(n-1)

# countdown(5)

# base case - condition that stops recursion, without this, function would call itself forever causing stack overflow error
# recursive case - function calls itself with a modified argument 

# example of base and recursive case

def factorial(n):
    # base case
    if n == 0 or n == 1:
        return 1
    # recursive case
    else:
        return n * factorial(n - 1)

print(factorial(5))

# calculating the sum all of numbers up to num
def sum_recursive(num):
    if num == 1: # base case
        return num
    return num + sum_recursive(num - 1) # recursive case 

print(sum_recursive(3))

# calculating the power of a number 
def power(base, exponent):
    if exponent == 0:
        return 1
    else: 
        return base * power(base, exponent - 1)
    
print(power(2, 4))

def fibonnaci(n):
    if n <= 1:
        return n
    else:
        return fibonnaci(n-1) + fibonnaci(n-2)
    
for i in range(10):
    print(f"fibonnaci sequence:",{fibonnaci(i)})