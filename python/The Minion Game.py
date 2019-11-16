def minion_game(string):
    string =  string.lower()
    vowels = ['a','e','i','u','o']
    Stuart = 0
    Kevin = 0
    for s in range(len(string)):
        if string[s] in vowels:
            Kevin += len(string)- s
        else: 
            Stuart += len(string) - s
    if Kevin > Stuart:
        print("Kevin",str(Kevin))
    if Stuart > Kevin:
        print("Stuart",str(Stuart))
    if Kevin == Stuart:
        print("Draw")


        

if __name__ == '__main__':
    s = input()
    minion_game(s)