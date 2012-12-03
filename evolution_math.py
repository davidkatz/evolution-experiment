import random
import string

# ------------------------------------------------------------------
# EVOLUTION MATH
# 
# Holds all kinds of helper functions. Rule of thumb is 'if it's not
# directly related to evolution, put it in here'
# ------------------------------------------------------------------


# Calculates the levenshtein distance between a and b. Lower levenshtein
# distances means more similar strings, with a score of 0 meaning an identical
# string. (taken from http://hetland.org/coding/python/levenshtein.py)
def levenshtein(a,b):
    n, m = len(a), len(b)
    if n > m:
        # Make sure n <= m, to use O(min(n,m)) space
        a,b = b,a
        n,m = m,n
        
    current = range(n+1)
    for i in range(1,m+1):
        previous, current = current, [i]+[0]*n
        for j in range(1,n+1):
            add, delete = previous[j]+1, current[j-1]+1
            change = previous[j-1]
            if a[j-1] != b[i-1]:
                change = change + 1
            current[j] = min(add, delete, change)
            
    return current[n]