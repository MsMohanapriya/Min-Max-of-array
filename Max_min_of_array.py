def MinMaxofArray(array):
    minimum_value=float('inf')
    maximum_value=(float('-inf'))
    
    for i in range(len(array)):
        if minimum_value>array[i]:
            minimum_value=array[i]
            
        if maximum_value<array[i]:
            maximum_value=array[i]
        
    return maximum_value+minimum_value
array=list(map(int,input().split()))
print(MinMaxofArray(array))
    
    