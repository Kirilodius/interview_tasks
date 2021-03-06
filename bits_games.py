def multiply(x, y):
    sum = 0
    while x:
        if x & 1:
           sum = add(sum, y)
        x >>= 1
        y <<= 1
    return sum
    

def add(x, y):
    k = 1
    carryIn = 0
    sum = 0
    tx = x
    ty = y
    while tx or ty:
        lx = x & k
        ly = y & k
        carryOut = (lx & ly) | (lx & carryIn) | (ly & carryIn)
        sum |= lx ^ ly ^ carryIn
        carryIn = carryOut << 1
        k <<= 1
        tx >>= 1
        ty >>= 1
        
    return sum | carryIn
    
def devide(div, divs):
    result = 0
    power = 32
    pdivs = divs << power
    
    while div >= divs:
        while pdivs > div:
            pdivs >>= 1
            power -= 1
        
        result += 1 << power
        div -= pdivs
    
    return result
