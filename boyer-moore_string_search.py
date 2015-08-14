def boyer_moore_search(pat, txt):
    if len(pat) > len(txt) or min(len(pat), len(txt)) == 0:
        return None
    
    stops = bStops(pat)
    prefixes = pref_func(pat)
    rprefixes = pref_func(pat[::-1])
    pref_table = []
    
    for i in range(len(pat) + 1):
        pref_table.append(prefixes[-1])
    
    for i in range(1, len(pat)):
        j = rprefixes[i]
        pref_table[j] = min(pref_table[j], i - j + 1)
    
    txt_offset = len(pat) - 1

    while txt_offset < len(txt):
        pat_offset = len(pat) - 1
        kof = txt_offset
        while txt[kof] == pat[pat_offset]:
            if pat_offset == 0:
                return kof
            kof -= 1
            pat_offset -= 1

        if (pat_offset == len(pat) - 1):
            txt_offset += stops.get(txt[txt_offset], len(pat))
        else:
            txt_offset += pref_table[len(pat) - pat_offset - 1]
    
    return -1
    

def bStops(pat):
    return dict([(l, len(pat) - pat.rfind(l) - 1) for l in pat[:-1]])
    

    
def pref_func(pat):
    p = [0 for i in range(len(pat))]
    k = 0
    for i in range(1, len(pat)):
        while (k > 0) and pat[k] != pat[i]:
            k = p[k - 1]
        if pat[k] == pat[i]:
            k += 1
        p[i] = k
    
    return p
                                                           
print(boyer_moore_search("abcabc", "abcabdabcabc"))
