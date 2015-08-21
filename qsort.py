def qsort(arr):
    rlIdxs = []
    
    rlIdxs.append(0)
    rlIdxs.append(len(arr) - 1)
    
    while len(rlIdxs) > 0:
        subsStart = rlIdxs.pop(0)
        subsEnd = rlIdxs.pop(0)
        
        if subsEnd < subsStart:
            continue
        
        lIdx = subsStart + 1
        pIdx = subsStart
        rIdx = subsEnd
        pElem = arr[pIdx]
        
        while lIdx < rIdx:
            while lIdx <= rIdx and arr[lIdx] <= pElem:
                lIdx += 1
            
            while lIdx <= rIdx and arr[rIdx] >= pElem:
                rIdx -= 1
                
            if rIdx >= lIdx:
                arr[rIdx], arr[lIdx] = arr[lIdx], arr[rIdx]
        
        if pIdx <= rIdx:
            if pElem > arr[rIdx]:
                arr[pIdx], arr[rIdx] = arr[rIdx], arr[pIdx]
        
        if subsStart < rIdx:
            rlIdxs.append(subsStart)
            rlIdxs.append(rIdx - 1)
        
        if subsEnd > rIdx:
            rlIdxs.append(rIdx + 1)
            rlIdxs.append(subsEnd)    
    
qsort([9, 8, 7, 6, 5, 4, 3, 2, 1])
