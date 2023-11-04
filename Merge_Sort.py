
def mergeSort(alist):

    if len(alist)>1:

    ## set middle of list 
        mid = len(alist)//2

    ## set variables to run through both lists 
        h = 0
        g = mid

    ## create two lists for each half of the list 
        lefthalf = []
        righthalf = []

    ## append the items of the list that are before the middle value 
        while h < mid:

            lefthalf.append(alist[h])
            h = h + 1

    ## append the middle value and items that are after it 
        while g < len(alist):
            righthalf.append(alist[g])
            g = g + 1

    ## recursively call function to sort each list individually
    ## until it only has one value left   
        mergeSort(lefthalf)
        mergeSort(righthalf)

    ## set initial variables to scan through lists by index 
        i=0
        j=0
        k=0
    
        while i < len(lefthalf) and j < len(righthalf):

    ## check to see which value is larger
            if lefthalf[i] <= righthalf[j]:

    ## append to list depending on condition
                alist[k]=lefthalf[i]
                i=i+1

            else:

                alist[k]=righthalf[j]
                j=j+1

            k=k+1

    ## append other values to list that will be recursively called 
        while i < len(lefthalf):

            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):

            alist[k]=righthalf[j]
            j=j+1
            k=k+1



