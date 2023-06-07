#QuickSort

def quicksort(array, inicio=0, fim=None):
    if(fim is None):
        fim = len(array) - 1
    
    if(inicio < fim):
        pivot = partition(array, inicio, fim)
        quicksort(array, inicio, pivot-1)
        quicksort(array, pivot+1, fim)

def partition(array, inicio, fim):
    pivot = array[fim]
    i = inicio
    for j in range(inicio, fim):
        if(array[j] <= pivot):
            array[j], array[i] = array[i], array[j]
            i = i + 1 

    array[i], array[fim] = array[fim], array[i]
    return i

data = [4,7,2,6,5,1,8,3]
quicksort(data)
print(data)