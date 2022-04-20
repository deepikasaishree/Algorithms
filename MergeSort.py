def mergeSort(arr):
    if len(arr)==1:
        return arr
    m=(len(arr)-1)//2
    l1=mergeSort(arr[:m+1])
    l2=mergeSort(arr[m+1:])
    res=merge(l1,l2)
    return res

def merge(l1,l2):
    i=0
    j=0
    l=[]
    while i<=len(l1)-1 and j<=len(l2)-1:
        if l1[i]<l2[j]:
            l.append(l1[i])
            i+=1
        else:
            l.append(l2[j])
            j+=1
    if i>len(l1)-1:
        while j<=len(l2)-1:
            l.append(l2[j])
            j+=1
    else:
        while i<=len(l1)-1:
            l.append(l1[i])
            i+=1
    return l



arr=[9,20,1,24,7]
print(mergeSort(arr))


#Complexity-O(nlog(n))