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

# def factorial(n):
    # base case
#    if n == 0 or n == 1:
#        return 1
    # recursive case
#    else:
#        return n * factorial(n - 1)

# print(factorial(5))


# def inception(dreams):
#    if dreams == 0:
#        return 
#    inception(dreams - 1)
#    print(f"this is dream {dreams} within a dream")

# inception(100)
