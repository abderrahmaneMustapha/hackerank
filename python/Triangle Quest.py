
"""
    repdigit number is a number like  d, dd, ddd, dddd, ...  that contains only 
    (zero or more times) the digit  d , with  0 < d < b  (in its base  b  representation).
    Generalized repdigit numbers (in base  b ) are numbers of the form
"""
#reference http://oeis.org/wiki/Repdigit_numbers
for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave
    print(int(i*(((10**i)-1)/9)))
    