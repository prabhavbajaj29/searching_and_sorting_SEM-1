def selection_sort(arr):
    for i in range(len(arr)):
        minimum_index=i

        for j in range(i+1,len(arr)):
            if arr[j]<arr[minimum_index]:
                minimum_index=j
        
        if i!=minimum_index:
            arr[i],arr[minimum_index]=arr[minimum_index],arr[i]

arr=[5,4,3,2,1]
selection_sort(arr)
print(arr)                  