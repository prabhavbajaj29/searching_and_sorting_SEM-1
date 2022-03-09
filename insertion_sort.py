def insertion_sort(arr):

    for i in range(1,len(arr)):
        value_to_sort=arr[i]

        while arr[i-1]>value_to_sort and i>0:
            arr[i],arr[i-1]=arr[i-1],arr[i]
            i=i-1

    return arr


arr=[5,4,3,2,1]
print(insertion_sort(arr))