
n = 4
mason_height = 5


heights = [2, 6, 2]
prices = [2, 3, 2]



def raceAgainstTime(n, mason_height, heights, prices):

    res = 0
    current_height = mason_height

    for i in range(n-1):
        cost = abs(current_height - heights[i])
        price = prices[i]
        if heights[i] > current_height:
            res += (cost + price)
            current_height = heights[i]
        elif cost + price < 0:
            res += (cost + price)
            current_height = heights[i]
        res += 1

    res += 1

    return res

print raceAgainstTime(n, mason_height, heights, prices)




