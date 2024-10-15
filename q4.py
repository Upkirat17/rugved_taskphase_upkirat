def selection_sort(string):
    
    list1=list(string)
    n=len(list1)

    for i in range(n):
        min_pos=i
        for j in range(i+1,n):
            if list1[j]<list1[min_pos]:
                min_pos=j

        list1[i], list1[min_pos]=list1[min_pos],list1[i]

    return ''.join(list1)