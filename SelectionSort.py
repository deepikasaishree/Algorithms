def selectionsort(A):
    n=len(A)
    for i in range(n-1):
        min_ind=i
        for j in range(i+1,n):
            if A[j]<A[min_ind]:
                min_ind=j
        A[i],A[min_ind]=A[min_ind],A[i]
    return A   

A=[1,19,12,2,5]
print(selectionsort(A))


#Complexity-O(n^2)