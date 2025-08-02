class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> sol = new ArrayList<>();
       
        for (int i = 0; i < numRows; i++) {
            if (i == 0) { 
                List<Integer> row = new ArrayList<>();
                row.add(1);
                sol.add(row);
            }
            else if (i == 0) { 
                List<Integer> row = new ArrayList<>();
                row.add(1); row.add(1);
                sol.add(row);
            }
            else {
                List<Integer> row = new ArrayList<>();
                row.add(1);
                List<Integer> prev = sol.get(sol.size() - 1);
                for (int j = 1; j < prev.size(); j++) {
                    row.add(prev.get(j - 1) + prev.get(j));
                }
                row.add(1);
                sol.add(row);

            }
            
        }
        return sol;
    }
}