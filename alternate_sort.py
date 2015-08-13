def resort(lst):
    for i in range(1, len(lst)):
        if ((i % 2 == 0 and lst[i] >= lst[i - 1])
            or (i % 2 != 0 and lst[i] <= lst[i - 1])):
            lst[i], lst[i - 1] = lst[i - 1], lst[i]
    
    return lst
