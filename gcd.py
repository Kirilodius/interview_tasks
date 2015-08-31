def gcd(x, y):
    if x == 0:
        return y
    
    if y == 0:
        return x
    
    if not (x & 0x1) and not (y & 0x1):
        return gcd(x >> 1, y >> 1) << 1
    
    elif not (x & 0x1) and y & 0x1:
        return gcd(x >> 1, y)
        
    elif x & 0x1 and not (y & 0x1):
        return gcd(x, y >> 1)
    
    else:
        if x > y:
            return gcd(x - y, y)
        else:
            return gcd(x, y - x)
            

print gcd(24, 300)
