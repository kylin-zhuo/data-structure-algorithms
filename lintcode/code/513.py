class Solution:
    """
    @param: n: a positive integer
    @return: An integer
    """
    def numSquares(self, n):
        # write your code here
        if n <= 1:
            return 1
        psquares = []
        i = 1
        while i*i <= n:
            psquares.append(i*i)
            i += 1
            
        count = 0
        goals = {n}

        while goals:
            count += 1
            temp = set()
            for g in goals:
                for d in psquares:
                    if g == d:
                        return count
                    if g < d:
                        break
                    temp.add(g-d)
            goals = temp

        return count