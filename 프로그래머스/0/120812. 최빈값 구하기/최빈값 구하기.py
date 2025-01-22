def solution(array):
    count = {}
    for num in array:
        count[num] = count.get(num, 0) + 1  
    
    max_count = max(count.values())  
    most = []  
    for key, value in count.items():  
        if value == max_count:  
            most.append(key) 
        
    if len(most) > 1: 
        return -1
    return most[0]  