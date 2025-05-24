class Solution {
    public List<Integer> findWordsContaining(String[] words, char x) {
        String s = Character.toString(x);
        LinkedList<Integer> list = new LinkedList<>();
        for (int i = 0; i < words.length; i++) {
            if (words[i].contains(s)) {
                list.add(i);
            }
        }
        return list;
    }
}