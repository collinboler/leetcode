import java.util.*;
class Record {
    int win;
    int loss;
    Record(int win, int loss) {
        this.win = win;
        this.loss = loss;
    }
}
class Solution {
    public List<List<Integer>> findWinners(int[][] matches) {
        HashMap<Integer, Record> map = new HashMap<>();
        
        for (int[] match : matches) {
            if (!map.containsKey(match[0])) {
                Record r = new Record(1, 0);
                map.put(match[0], r);
            }
            else {
                Record r = map.get(match[0]);
                r.win++;
                map.put(match[0], r);
            }
            
            if (!map.containsKey(match[1])) {
                Record r = new Record(0, 1);
                map.put(match[1], r);
            }
            else {
                Record r = map.get(match[1]);
                r.loss++;
                map.put(match[1], r);
            }
        }
        List<Integer> oneL = new ArrayList<>();
        List<Integer> noL = new ArrayList<>();
        
        for (Integer key: map.keySet()) {
            // System.out.println(key + " (" + map.get(key).win + ", " + map.get(key).loss + ")");
            if (map.get(key).loss == 0) noL.add(key);
            else if (map.get(key).loss == 1) oneL.add(key);
        }
        List<List<Integer>> sol = new ArrayList<>();
        Collections.sort(noL);
        Collections.sort(oneL);
        sol.add(noL);
        sol.add(oneL);


        
        return sol;
           
            
            
        
    }
}