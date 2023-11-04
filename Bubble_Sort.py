def bubbleSort(alist):
    
    # make (length - 1) comparisons between items in the list each pass
    # runs until list is only 1 item (i.e (length-2) comparisons second pass)
    for passnum in range(len(alist)-1,0,-1):

        #iterate over items w/in range of list 
        for i in range(passnum):

            # if the currently ID item is > the next item:
            if alist[i] > alist[i+1]:

                # the current item switches places with the next item
                # largest value gets added to the end of list each pass
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                


