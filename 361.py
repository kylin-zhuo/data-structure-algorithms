class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        # establish four cumulative arrays for the four directions

        [{'0': [{'0': [{'0': [{'1': [{'1': [{'0': [{'0': [{'1': [{}, 9]}, 8]}, 7]}, 6]}, 5], '0': [{'1': [{'0': [{'1': [{'0': [{}, 9]}, 8], '0': [{'0': [{}, 9]}, 8]}, 7]}, 6], '0': [{'1': [{'0': [{'1': [{}, 9]}, 8]}, 7], '0': [{'1': [{'1': [{}, 9], '0': [{}, 9]}, 8]}, 7]}, 6]}, 5]}, 4]}, 3]}, 2]}, 1]
