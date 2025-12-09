class LRUCache {
    LinkedList<Integer> timeManager; // manager which keys are removed
    int capacity;
    int storage;
    HashMap<Integer, Integer> map;
    public LRUCache(int capacity) {
        // System.out.println("init, cap: " + capacity);
        this.timeManager = new LinkedList<>();
        this.capacity = capacity;
        this.storage = 0;
        this.map = new HashMap<>();
    }
    // return if exists
    public int get(int key) {
        // System.out.println("Get(Key: " + key + ")");

        if (map.containsKey(key)) {
            timeManager.remove(Integer.valueOf(key));
            timeManager.add(key);
            return map.get(key);
        }
        return -1; // if no key in map
    }
    
    public void put(int key, int value) {
        // System.out.println("Put(Key: " + key + ", Val: " + value + ")");
        if (map.containsKey(key)) {
            map.put(key, value);
            
            this.timeManager.remove(Integer.valueOf(key));
            this.timeManager.add(key);
            return;
        }
        if (this.storage == this.capacity) {
            int fatKey = this.timeManager.removeFirst();
            System.out.println(fatKey);
            map.remove(fatKey);
            System.out.println(map.containsKey(fatKey));
            this.storage--;
        }
        map.put(key, value);
        this.storage++;
        this.timeManager.add(key);
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity = 2);
 * int param_1 = obj.get(key);
 * obj.put(key,value);

put(1,1);
put(2,2);



 */