from math import *
def demo(x):
    '''
    This is a demo function
    Where in you just return square of the number
    args:
        x (int)
    returns:
        x*x (int)
    '''

    ## Code Here
    return x * x
def is_palindrome(string):
    '''
    This function returns True if the given string is
    a Palindrome
    args:
        string (str)
    returns:
        flag (bool)
    '''
    ## Code Here
    string = string.lower()
    a = len(string)
    k = 0
    for i in range(round(a / 2)):
        if string[i] == string[a - i - 1]:
            k += 1
    return (k == round(a / 2))

def sqrt_of_numbers(num):
    '''
    This function returns the magnitude of the square root of the number
    args:
        num (int) Need not be positive
    returns:
        sqroot (float)
    '''
    if num < 0:
        num=abs(num)
        a=complex(0,sqrt(num))
    else:
        a = sqrt(num)
    ## Code Here
    return a

def Maximum(arr):
    '''
    This function returns first maximum and the second maximum
    number in the array
    args:
        arr (list)
    returns:
        Max1, Max2 (int, int)
    '''
    ## Code Here
    a = max(arr)
    arr.remove(a)
    return a, max(arr)

def even_sort(arr):
    '''
    This function sorts the array giving higher preference to even numbers
    args:
        arr (list)
    returns:
        sort_arr (list)
    ex:
        arr = [15, 2, 6, 88, 7]
        ## then
        sort_arr = [2, 6, 88 ,7 ,15]
        ## This is any even number is smaller than any odd number
    '''

    ## Code Here
    odd = []
    even = []
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            a = arr[i]
            even.append(a)
        else:
            a = arr[i]
            odd.append(a)
    even.sort()
    odd.sort()
    even.extend(odd)
    return even

#print
def eqn_solver(a, b, c):
    '''
    This function solves a two variable system
    i.e.,
        A = [ 1, 2 ]
        B = [ 3, 4 ]
        C = [ 5, 6 ]
        then it means
        1x + 3y = 5
        2x + 4y = 6
        Hence you are required to find x, y for such a linear system
    args:
        A, B, C (list, list, list) representing coefficients in the equation
    returns:
        x, y (float, float)
    '''
    ## Code Here
    x = ((b[1] * c[0]) - (b[0] * c[1])) / ((b[1] * a[0]) - (b[0] * a[1]))
    y = ((c[1] * a[0]) - (c[0] * a[1])) / ((b[1] * a[0]) - (b[0] * a[1]))

    return x, y