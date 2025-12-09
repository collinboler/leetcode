class Solution {
    private String alpha(String s) {
        // System.out.println("og string: " + s);
        char[] charray = s.toCharArray();
        Arrays.sort(charray);
        // System.out.println("changed string: " + new String(charray));

        return new String(charray);
    }
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> map = new HashMap<>();
        
        for (String s : strs) {
            if (map.containsKey(alpha(s))) {
                // check for duplicate
                map.get(alpha(s)).add(s); // add to the list in the hashmap
            }
            else { // populate new list
                List<String> list = new ArrayList<String>();
                list.add(s);
                map.put(alpha(s), list);
            }
        }
        List<List<String>> result = new ArrayList<List<String>>();
        for (String key : map.keySet()) {
            result.add(map.get(key));
        }
        return result;
    }
}