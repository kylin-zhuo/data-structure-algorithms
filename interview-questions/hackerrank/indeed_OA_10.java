import java.util.List;
import java.util.*;

public class Rateing {

    public static void main(String[] argv){

        System.out.println("Please enter: ");
        Scanner scanner = new Scanner(System.in);
        List<Integer> rates = new ArrayList<>();
        List<Integer> managerIds = new ArrayList<>();
        Map<Integer, List<Integer>> idMap = new HashMap<>();
        
        int rootId = -1;
        int id = 0;
        
        while(scanner.hasNextInt()) {
            int curRate = scanner.nextInt();
            int curMid = scanner.nextInt();
            rates.add(curRate);
            managerIds.add(curMid);

            idMap.putIfAbsent(curMid, new ArrayList<>());
            idMap.get(curMid).add(id);

            if(curMid == -1) {
                rootId = id;
            }
            id ++;
        }
        scanner.close();

        for(int rate : rates) {
            System.out.println("Rate is: " + rate);
        }
        System.out.println("---------------------------------");
        
        Queue<Integer> q = new LinkedList<>();
        q.add(rootId);

        while(!q.isEmpty()) {
            int cur = q.poll();
            if(idMap.containsKey(cur)) {
                int curRate = rates.get(cur);
                for(int child : idMap.get(cur)) {
                    if(rates.get(child) > curRate) {
                        rates.set(child, curRate);
                    }
                    q.offer(child);
                }
            }
        }
        for(int rate : rates) {
            System.out.println("Rate is: " + rate);
        }
    }
}