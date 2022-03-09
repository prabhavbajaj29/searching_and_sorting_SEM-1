def merge_sort(arr):
    if len(arr)<=1:
        return arr

    mid=len(arr)//2

    left=arr[:mid]
    right=arr[mid:]

    left=merge_sort(left)
    right=merge_sort(right)

    return merge_two_sorted_lists(left,right)

def merge_two_sorted_lists(a,b):
    sorted_list=[]
    len_a=len(a)
    len_b=len(b)

    i=0
    j=0

    while (i<len_a) and (j<len_b):
        if a[i]<=b[j]:
            sorted_list.append(a[i])
            i+=1
        else:
            sorted_list.append(b[j])
            j+=1

    while i<len_a:
        sorted_list.append(a[i])
        i+=1
    while j<len_b:
        sorted_list.append(b[j])
        j+=1            
    return sorted_list


arr=[12,31,45,2,1,0,66,121,58,25]
print(merge_sort(arr))                