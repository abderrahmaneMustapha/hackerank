from collections import OrderedDict 

def merge_the_tools(string, k):
    t = [print(''.join(OrderedDict.fromkeys(string[i:i+k]))) for i in range(0,len(string),k)]
   
