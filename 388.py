class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        maxv = 0
        dic = {-1: 0}
        
        for line in input.splitlines():
            
            name = line.lstrip('\t')
            depth = len(line) - len(name)
            print name
            
            if '.' in name:
                maxv = max(maxv, dic[depth - 1] + len(name))
            else:
                dic[depth] = dic[depth - 1] + len(name) + 1
            
        return maxv