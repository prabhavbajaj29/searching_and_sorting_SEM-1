def quick_sort(arr):
    len_arr=len(arr)

    if len_arr<=1:
        return arr

    else:
        pivot=arr.pop()

    items_greater=[]
    items_less=[]

    for item in arr:
        if item>pivot:
            items_greater.append(item)
        else:
            items_less.append(item)

    return quick_sort(items_less)+[pivot]+quick_sort(items_greater)

arr=[12,3,8,8,2,2,56,45]

print(quick_sort(arr))