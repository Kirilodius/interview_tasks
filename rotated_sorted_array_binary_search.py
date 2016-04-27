def find(arr, val):
    sIdx = 0
    eIdx = len(arr) - 1
    
    while sIdx <= eIdx:
        pIdx = sIdx + ((eIdx - sIdx) / 2)
        p = arr[pIdx]
        if p == val:
            return pIdx
        
        if p >= arr[sIdx] and p <= arr[eIdx]:
        	if p > val:
        		eIdx = pIdx
        	else:
        		sIdx = pIdx + 1

        else:
            if arr[sIdx] <= val:
            	return find(arr[:pIdx], val)
            else:
            	return find(arr[pIdx + 1:], val)
    return -1



print find([4, 5, 6, 1, 2], 1)
print find([4, 5, 6, 1, 2], 2)
print find([4, 5, 6, 1, 2], 3)
print find([4, 5, 6, 1, 2], 4)
print find([4, 5, 6, 1, 2], 5)
print find([4, 5, 6, 1, 2], 6)

print find([4, 5, 0, 1, 2], 4)
print find([4, 5, 0, 1, 2], 5)

print find([4, 5, 0, 1, 2], 1)
print find([4, 5, 0, 1, 2], 2)

print find([1, 2, 3, 4, 5, 6], 6)
print find([1, 2, 3, 4, 5, 6], 1)
