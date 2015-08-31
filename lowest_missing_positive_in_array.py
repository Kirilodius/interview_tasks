def find_lowest_missing(lst):
    i = 0
    while i < len(lst) - 1:
        if (lst[i] > 0
        and lst[i] <= len(lst)
        and lst[i] != lst[lst[i] - 1]):
            tmpIdx = lst[i] - 1
            lst[i] = lst[tmpIdx]
            lst[tmpIdx] = tmpIdx + 1
        else:
            i += 1

    for i in range(len(lst)):
        if lst[i] != i + 1:
            return i + 1

print find_lowest_missing([4, 3, 0, 2])
