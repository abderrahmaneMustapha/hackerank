N = int(input())
n = int(input())

def divmod(N,n):
    d = int(N/n)
    m = N%n
    print(str(d)+"\n"+str(m))
    return (d, m)


print(divmod(N,n))