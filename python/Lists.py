if __name__ == '__main__':
    N = int(input())
L = []
for _ in range(N):
    act, *inp = input().split()
    i = 0
    e = 0
    if(len(inp) == 1):
        e  =  int(inp[0])
    if(len(inp) == 2):
        i =  int(inp[0])
        e = int(inp[1])
    if act=="insert":
        L.insert(i,e)
    if act=="remove":
        L.remove(e)
    if act=="append":
        L.append(e)
    if act=="sort":
        L.sort()
    if act=="pop":
        L.pop()
    if act=="reverse":
        L.reverse()
    if act=="print":
        print(L)
        
    

    

