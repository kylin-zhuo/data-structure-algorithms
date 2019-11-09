/**
 * Definition for Directed graph.
 * class DirectedGraphNode {
 *     int label;
 *     ArrayList<DirectedGraphNode> neighbors;
 *     DirectedGraphNode(int x) { label = x; neighbors = new ArrayList<DirectedGraphNode>(); }
 * };
 */

public class Solution {
    /*
     * @param graph: A list of Directed graph node
     * @return: Any topological order for the given graph.
     */
    public ArrayList<DirectedGraphNode> topSort(ArrayList<DirectedGraphNode> graph) {
        // write your code here
        ArrayList<DirectedGraphNode> res = new ArrayList<DirectedGraphNode>();
        if (graph == null) return res;
        Map<DirectedGraphNode, Integer> inDegrees = getIndegrees(graph);
        Queue<DirectedGraphNode> queue = new LinkedList<DirectedGraphNode>();
        for (DirectedGraphNode node:graph) {
            if (inDegrees.get(node) == 0) queue.offer(node);
        }
        while (!queue.isEmpty()) {
            DirectedGraphNode node = queue.poll();
            res.add(node);
            for(DirectedGraphNode n:node.neighbors) {
                inDegrees.put(n, inDegrees.get(n) - 1);
                if (inDegrees.get(n) == 0) queue.offer(n);
            }
        }
        return res;
        
    }
    
    private Map<DirectedGraphNode, Integer> getIndegrees(ArrayList<DirectedGraphNode> graph) {
        Map<DirectedGraphNode, Integer> degrees = new HashMap<>();
        
        for (DirectedGraphNode node : graph) {
            degrees.put(node, 0);
        }
    
        for (DirectedGraphNode node : graph) {
            for (DirectedGraphNode neighbor : node.neighbors) {
                degrees.put(neighbor, degrees.get(neighbor)+1);
            }
        }
        return degrees;
    }
}