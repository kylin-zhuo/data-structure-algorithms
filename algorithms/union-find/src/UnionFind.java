import java.util.HashMap;

class UnionFind {

	private int[] parent;

	private int[] groupSize;

	private int nGroups;

	private int nElements;

	private HashMap<String, Integer> elementNameMap;

	public UnionFind() {
		this.elementNameMap = new HashMap<>();
	}

	public UnionFind(int nElements) {
		// without element names
		this.nElements = nElements;
		this.parent = new int[nElements];
        this.groupSize = new int[nElements]; 
        for (int i = 0; i < nElements; i++){
            parent[i] = i;
            groupSize[i] = 1;
        }
	}

	public UnionFind(int nElements, String[] elementNames) {
		// self-defined element names
		if (nElements != elementNames.length) {
			throw IllegalArgumentException("the size doesn't match.");
		}
		this.nElements = nElements;
		this.parent = new int[nElements];
		this.groupSize = new int[nElements];
		// number the element names
		for (int i = 0; i < nElements; i++) {
			String elementName = elementNames[i];
            this.elementNameMap.put(elementName, i);
            parent[i] = i;
            groupSize[i] = 1;
		}
    }
    
    // union two components
    public void union(int a, int b) {
        int rootA = find(a);
        int rootB = find(b);
        if (rootA == rootB) {
            return;
        }
        if (groupSize[rootA] < groupSize[rootB]) {
            groupSize[rootB] += groupSize[rootA];
            parent[rootA] = rootB;
        } else {
            groupSize[rootA] += groupSize[rootB];
            parent[rootB] = rootA;
        }
        nGroups -= 1;
    }

    public int find(int id) {
        int root = id;
        while (parent[root] != root) {
            root = parent[root];
        }

        // path compression
        while(id != root) {
            int next = parent[id];
            parent[id] = root;
            id = next;
        }

        return root;
    }

    // overwrite for String
    public int find(String name) {
        return find(elementNameMap.get(name));
    }

    public boolean isConnected(int a, int b) {
        return find(a) == find(b);
    }

    public int getGroupSize(int i) {
        return groupSize[find(i)];
    }


    


    // getters and setter
    public int[] getParent() {
        return parent;
    }

    public void setParent(int[] parent) {
        this.parent = parent;
    }

    public int[] getGroupSize() {
        return groupSize;
    }

    public void setGroupSize(int[] groupSize) {
        this.groupSize = groupSize;
    }

    public int getnGroups() {
        return nGroups;
    }

    public void setnGroups(int nGroups) {
        this.nGroups = nGroups;
    }

    public int getnElements() {
        return nElements;
    }

    public void setnElements(int nElements) {
        this.nElements = nElements;
    }

    public HashMap<String, Integer> getElementNameMap() {
        return elementNameMap;
    }

    public void setElementNameMap(HashMap<String, Integer> elementNameMap) {
        this.elementNameMap = elementNameMap;
    }

    


}