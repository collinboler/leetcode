class Solution {
    public int scoreOfString(String s) {
        char[] sArr = s.toCharArray();
        int score = 0;
        for (int i = 0; i < s.length() - 1; i++) {
            
            score += Math.abs((int) sArr[i] - sArr[i + 1]);
        }
        return score;
    }
}