from collections import Counter
def solution(X, Y):
    arr= list((Counter((int(i) for i in X)) & Counter((int(j) for j in Y))).elements())
    arr.sort(reverse=True)
    if len(arr) == 0:
        return "-1"
    if arr[0] == 0:
        return "0"
    return ''.join(map(str,arr))
    
    
    
    
    
        
  
            
        