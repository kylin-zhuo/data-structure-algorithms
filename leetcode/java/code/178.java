public class Solution {
    /*
     * @param n: An integer
     * @param edges: a list of undirected edges
     * @return: true if it's a valid tree, or false
     */
    public boolean validTree(int n, int[][] edges) {
        // write your code here
        if (edges.length != n - 1) return false;
        int[][] map = new int[n][n];
        
        for (int i = 0; i < edges.length; i++) {
            int v1 = edges[i][0], v2 = edges[i][1];
            map[v1][v2] = 1;
            map[v2][v1] = 1;
        }
        
        boolean[] visited = new boolean[n];
        dfs(map, 0, visited);
        
        for (int i = 0; i < visited.length; i++) {
            if (!visited[i]) return false;
        }
        return true;
    }
    
    private void dfs(int[][] map, int curr, boolean[] visited) {
        visited[curr] = true;
        for (int i = 0; i < map[curr].length; i++) {
            if (map[curr][i] != 0 && !visited[i]) dfs(map, i, visited);
        }
    }
}