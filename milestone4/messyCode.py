# Clear Code
# Has clear function title
# Less condenesed
# Clear indentataion
# Logic seperated into individual lines  
def factorial(n):
    if (n==1): 
        return n
    else:
        return n * factorial(n-1)

# Non-clear code
# Unclear function name (not clear what function does)
# Over condensed
# No spaces between operands (or in areas which would make code clearer)
def f(n):
    if n<=1:return 1; 
    else: return n*f(n-1)

print(f(4))
print(factorial(4))
