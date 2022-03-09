def binary_search(arr,item):
    start=0
    end=len(arr)-1

    mid=start+(end-start)//2

    while (start<=end):
        if arr[mid]==item:
            return mid

        elif arr[mid]>item:
            end=mid-1

        else:
            start=mid+1
        mid=start+(end-start)//2

    return -1

arr=[8,6,4,2]

arr.sort()

item=int(input("Enter the element you want to find: "))

print(binary_search(arr,item))


