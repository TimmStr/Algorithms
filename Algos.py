



def bubble(arr):
    for i in range(0,len(arr)-1):
        test = True
        for j in range(0,len(arr)-1):
            if(arr[j]>arr[j + 1]):
                cache = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = cache
                test = False
        if test == True:
            return arr
arr = [5,3,9,6,2,12]
print(bubble(arr))

def insertion(arr):
    for i in range (0,len(arr)-1):
        sortierenderwert = arr[i]
        j=i
        while(j > 0) and (arr[j-1]>sortierenderwert):
            placeholder = arr[j]
            arr[j]=arr[j-1]
            arr[j-1]=placeholder
            j=j-1
    return arr
arr = [5,3,9,6,2,12]
print(insertion(arr))

