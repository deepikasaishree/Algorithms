def bubblesort(A):
    swap=False
    for i in range(len(A)-1,0,-1):
        for j in range(i):
            if A[j]>A[j+1]:
                A[j],A[j+1]=A[j+1],A[j]
                swap=True
        if swap:
            swap=False
        else:
            break
    return A

A=[24,19,12,3,1]
print(bubblesort(A))

#Time Complexity-O(n^2)