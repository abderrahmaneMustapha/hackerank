if __name__ == '__main__':
    arr = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append({'name': name, 'score': score})
    def by_score(arr):
        return arr['score']
    arr.sort(key=by_score)
    
    def min2(arr):
        result = []
        low = arr[0]['score']
        state= 0
        for a in arr:
            if a['score']!=low and state == 0:
                low = a['score']                
                state = 1
            if a['score']== low and state == 1:
                result.append(a)
        return result
    def by_name(arr):
        return arr['name']
        
    #final result
    f_r = min2(arr)
    f_r.sort(key=by_name)
    for f in f_r:
        print(f['name'])
