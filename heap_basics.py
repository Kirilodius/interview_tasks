def make_heap(lst):
    for leaf in range(len(lst) / 2, -1, -1):
        heapify(leaf, lst)


def heapify(idx, lst):
    lLen = len(lst)

    while True:
        max  = idx
        lIdx = left(idx)
        rIdx = right(idx)
        
        if lIdx < lLen and lst[lIdx] > lst[max]:
            max = lIdx
        
        if rIdx < lLen and lst[rIdx] > lst[max]:
            max = rIdx
            
        if max == idx:
            break
        
        lst[idx], lst[max] = lst[max], lst[idx]
        idx = max

        
def pop_max(lst):
    max = lst[0]
    lst[0], lst[len(lst) - 1] = lst[len(lst) - 1], lst[0]
    del lst[len(lst) - 1]
    heapify(0, lst)
    return max
    

def push(nVal, lst):
    lst.append(nVal)
    idx = len(lst) - 1
    pIdx = (idx - 1) / 2
    
    while pIdx >= 0 and lst[pIdx] < lst[idx]:
        lst[pIdx], lst[idx] = lst[idx], lst[pIdx]
        idx = pIdx
        pIdx = (idx - 1) / 2
        


def left(idx):
    return idx * 2


def right(idx):
    return idx * 2 + 1
    

lst = [1, 2, 3, 4, 5, 6, 7, 8]

make_heap(lst)
push(9, lst)
for i in range(len(lst)):
    print pop_max(lst)
