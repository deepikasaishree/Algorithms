def quickSort(arr):
    if len(arr)>1:
        pivot=arr.pop()
        greaterList,equalList,smallerList=[],[pivot],[]
        for i in arr:
            if i==pivot:
                equalList.append(i)
            elif i>pivot:
                greaterList.append(i)
            else:
                smallerList.append(i)
        return quickSort(smallerList)+equalList+quickSort(greaterList)
    else:
        return arr

if __name__=="__main__":
    arr=[24,21,22,32,40]
    print(quickSort(arr))


#Complexity-O(n^2)