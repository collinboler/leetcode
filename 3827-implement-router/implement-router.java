import java.util.*;

class Router {
    Deque<int[]> q;
    Map<Integer,List<int[]>> map;
    int size;

    public Router(int memoryLimit) {
        q=new LinkedList<>();
        map=new HashMap<>();
        size=memoryLimit;
    }

    public boolean addPacket(int source,int destination,int timestamp) {
        map.putIfAbsent(destination,new ArrayList<>());
        List<int[]> list=map.get(destination);
        int left=lowerBound(list,timestamp);
        for(int i=left;i<list.size()&&list.get(i)[1]==timestamp;i++){
            if(list.get(i)[0]==source) return false;
        }
        list.add(new int[]{source,timestamp});
        q.addLast(new int[]{source,destination,timestamp});
        if(q.size()>size) forwardPacket();
        return true;
    }

    public int[] forwardPacket() {
        if(q.isEmpty()) return new int[0];
        int[] arr=q.pollFirst();
        map.get(arr[1]).remove(0);
        return arr;
    }

    public int getCount(int destination,int start,int end) {
        if(!map.containsKey(destination)) return 0;
        List<int[]> list=map.get(destination);
        int l=lowerBound(list,start), r=upperBound(list,end);
        if(l>r) return 0;
        return r-l+1;
    }

    private int lowerBound(List<int[]> list,int val){
        int l=0,r=list.size()-1;
        while(l<=r){
            int m=l+(r-l)/2;
            if(list.get(m)[1]>=val) r=m-1;
            else l=m+1;
        }
        return l;
    }

    private int upperBound(List<int[]> list,int val){
        int l=0,r=list.size()-1;
        while(l<=r){
            int m=l+(r-l)/2;
            if(list.get(m)[1]>val) r=m-1;
            else l=m+1;
        }
        return r;
    }
}


/**
 * Your Router object will be instantiated and called as such:
 * Router obj = new Router(memoryLimit);
 * boolean param_1 = obj.addPacket(source,destination,timestamp);
 * int[] param_2 = obj.forwardPacket();
 * int param_3 = obj.getCount(destination,startTime,endTime);
 */