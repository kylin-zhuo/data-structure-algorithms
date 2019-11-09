public class Solution {
    /*
     * @param numCourses: a total of n courses
     * @param prerequisites: a list of prerequisite pairs
     * @return: true if can finish all courses or false
     */
    
    class Course {
        ArrayList<Course> succs = new ArrayList<Course>();
        int id;
        Course(int id) { this.id = id; }
    }
    
    Map<Course, Integer> getIndegrees(List<Course> courses) {
        Map<Course, Integer> map = new HashMap<>();
        for (Course c:courses) {
            for (Course s:c.succs) {
                if (map.containsKey(s)) map.put(s, map.get(s)+1);
                else map.put(s, 1);
            }
        }
        return map;
    }
     
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        // write your code here
        List<Course> courses = new ArrayList<Course>();
        for (int i = 0; i < numCourses; i++) {
            courses.add(new Course(i));
        }
        for (int i = 0; i < prerequisites.length; i++) {
            int[] pair = prerequisites[i];
            courses.get(pair[1]).succs.add(courses.get(pair[0]));
        }
        Map<Course, Integer> inDegrees = getIndegrees(courses);
        Queue<Course> queue = new LinkedList<Course>();
        for (Course c:courses) {
            if (!inDegrees.containsKey(c)) queue.offer(c);
        }
        while (!queue.isEmpty()) {
            Course c = queue.poll();
            for (Course n:c.succs) {
                inDegrees.put(n, inDegrees.get(n) - 1);
                if (inDegrees.get(n) == 0) queue.offer(n);
            }
        }
        for (Course c:courses) {
            if (inDegrees.containsKey(c) && inDegrees.get(c) > 0) return false;
        }
        return true;
    }
}