class Solution {
    private String alpha(String s) {
        char[] charray = s.toCharArray();
        Arrays.sort(charray);
        return new String(charray);
    }
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> map = new HashMap<>(); 
        for (String s : strs) {
            String alphaS = alpha(s);
            if (map.containsKey(alphaS)) {
                // check for duplicate
                map.get(alphaS).add(s); // add to the list in the hashmap
            }
            else { // populate new list
                List<String> list = new ArrayList<String>();
                list.add(s);
                map.put(alphaS, list);
            }
        }
        List<List<String>> result = new ArrayList<List<String>>();
        for (String key : map.keySet()) {
            result.add(map.get(key));
        }
        return result;
    }
}