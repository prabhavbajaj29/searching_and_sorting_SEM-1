def first_occurence(arr,item):
    start=0
    end=len(arr)-1
    mid=start+(end-start)//2

    first=-1  #if element doesn't exist return -1

    while (start<=end):

        if arr[mid]==item:
            first=mid
            end=mid-1
        elif arr[mid]>item:
            end=mid-1
        else:
            start=mid+1
        
        mid=start+(end-start)//2
    return first

def last_occurence(arr,item):
    start=0
    end=len(arr)-1
    mid=start+(end-start)//2

    last=-1  #if element doesn't exist return -1

    while (start<=end):

        if arr[mid]==item:
            last=mid
            start=mid+1
        elif arr[mid]>item:
            end=mid-1
        else:
            start=mid+1
        
        mid=start+(end-start)//2
    return last

arr=[1,2,2,2,2,3,3,3,3,4,4,4,4,4,5,5,5,6,7,7,8,9,10]

item=int(input("Enter the element: "))

print("The first occurence of",item,"is: ",first_occurence(arr,item))

print("The last occurence of",item,"is: ",last_occurence(arr,item))


#To count the total number of occurences of an element

f=first_occurence(arr,item)
l=last_occurence(arr,item)

total_occurence=l-f+1

print("The total number of occurence of the",item,"is: ",total_occurence)


