def linear_search(arr,item):
    for i in range(len(arr)):
        if arr[i]==item:
            return i
    return -1     

arr=[1,2,1,3,4,5,6,21]
item=int(input())
print(linear_search(arr,item))
