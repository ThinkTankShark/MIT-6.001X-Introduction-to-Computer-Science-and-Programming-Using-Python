def satisfiesF(L):
       """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements
    Returns the length of L after mutation
    """

    myList = []
    for index in range(len(L)):
        word = L[index]

        if f(word) == True:
            myList.append(word)

    L[:] = myList         # uncovers the global variable

    return len(L)

run_satisfiesF(L, satisfiesF) 


## Use the following code for testing
## it should print
##2
##['a', 'a']
##_____________
##def f(s):
##       return 'a' in s
##
##              
##       print satisfiesF(L)
##       print L
