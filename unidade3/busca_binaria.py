#recursividade babyyy

def binary_search(array,item,begin=0,end=None):
    if end is None:
        end = len(array)
    if begin <= end:
        m = (begin + end) // 2
        if array[m] == item:
            return m
        if item < array[m]:
            return binary_search(array,item,begin, m-1)
        if item > array[m]:
            return binary_search(array,item, m+1, end)
    
    return None
  
lista = [2,3,4]
print(binary_search(lista,3))
