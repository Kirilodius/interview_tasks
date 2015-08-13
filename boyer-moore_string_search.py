def boyer_moore_search(pat, txt):
    stops = bStops(pat)
    print stops
    

def bStops(pat):
    return dict([(l, pat[:-1].rfind(l) + 1) for l in pat[:-1]])
    
def bSuffix(pat):
    pi = pref_func(pat)
    pi1 = pref_func(pat[::-1])
    suffshift = [0 for i in range(len(pat))]
    for i in range(len(pat)):
        suffshift[i] = len(pat) - pi[len(pat) - 1]

    for i in range(1, len(pat)):
        idx = len(pat) - 1 - pi1[i]
        suffshift[i] = min(suffshift[idx], i - pi1[i])
    
    return suffshift
    
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

boyer_moore_search("abc", "abc")
bSuffix("колокол")
