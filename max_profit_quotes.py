def maxProfit(quotes):
    min_price = 1000
    max_profit = 0
    for q in quotes:
        profit_from_next = q - min_price
        min_price = min(q, min_price)
        max_profit = max(profit_from_next, max_profit)
        
maxProfit([310, 315, 275, 295, 260, 270, 290, 230, 255, 250])
