class Solution {
    public List<Integer> findWordsContaining(String[] words, char x) {
            List<Integer> list = new ArrayList<>(words.length);
        for (int i = 0; i < words.length; i++) {
            for (char c : words[i].toCharArray()) {
                if (c == x) {
                    list.add(i);
                    break;
                }
            }
        }
        return list;
    }
}