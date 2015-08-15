def DutchFlagPartition(index, ar):
    pivot = ar[index]
    smaller, equal, unclass = 0, 0, 0
    larger = len(ar) - 1
    
    while equal <= larger:
        if ar[equal] < pivot:
            if equal != smaller:
                ar[equal], ar[smaller] = ar[smaller], ar[equal]
            smaller += 1
            equal += 1
        elif ar[equal] == pivot:
            equal += 1
        else:
            
            tl = larger
            ar[equal], ar[tl] = ar[larger], ar[equal]
            larger -= 1
    
    return ar
        
DutchFlagPartition(3, [1,5,3,2,1])
