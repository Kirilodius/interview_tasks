def maxProfit(quotes):
    min_price = 1000
    max_profit = 0
    for q in quotes:
        profit_from_next = q - min_price
        min_price = min(q, min_price)
        max_profit = max(profit_from_next, max_profit)
        
maxProfit([310, 315, 275, 295, 260, 270, 290, 230, 255, 250])

"""
Takes an array of int and return the length of longest subarray equal values
@note: fromt 310, 315, 275, 275, 275, 270, 290, 230, 255, 250 it returns 3 - as the length of longest sequance of same keys
@arr: array
"""
def maxLength(arr):
    max_length = 0
    p_i = arr[0]
    
    length = 0
    for i in arr[1:]:
        if i == p_i:
            length += 1
        else:
            length = 1
        max_length = max(length, max_length)
        
        p_i = i
    
    return max_length
        
        
maxProfit([310, 315, 275, 275, 275, 270, 290, 230, 255, 250])
