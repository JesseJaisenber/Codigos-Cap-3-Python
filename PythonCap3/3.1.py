arr = [11,4,51,22,45,2,4,5]

band = False
while band == False:
    band = True
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            aux = arr[i]
            arr[i] = arr [i+1]
            arr[i + 1] = aux
            band = False
            
print(arr)