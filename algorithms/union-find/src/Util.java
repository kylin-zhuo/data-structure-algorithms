public class Util {

    public static void main(String[] args) {
        System.out.println("Union Find util begins");
        
        UnionFind uf = new UnionFind(8);
        uf.union(1, 2);
        uf.union(3, 5);
        uf.union(4, 6);
        uf.union(0, 7); 
        for (int i = 0; i < uf.getParent().length; i++) {
            System.out.print(uf.getParent()[i] + " ");
        }
        System.out.println(uf.getnGroups());
    }
}

