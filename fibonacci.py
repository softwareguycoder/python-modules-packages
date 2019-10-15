# fibonacci.py

import sys

FIB_MAX = 1000
print("Inside the fibonacci module!")

def fib(n):
    """Return Fibonacci series up to n (max FIB_MAX) as a list"""
    n = min(n, FIB_MAX)
    results = []
    a = 0
    b = 1
    while b < n:
        results.append(b)
        a, b = b, a+b
        
    return results
    

def fib2(n):
    """Print Fibonacci series up to n"""
    print(" ".join([str(k) for k in fib(n)]))
    

# The following section is only executed if this module is 
# launched directly from the command line by the user.
if __name__=="__main__":
    if len(sys.argv) != 2:
        print("USAGE: %s <maxnum>" % (sys.argv[0]))
        sys.exit(-1)
    fib2(int(sys.argv[1]))
