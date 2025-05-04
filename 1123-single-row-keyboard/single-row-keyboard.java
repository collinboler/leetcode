class Solution {
    public int calculateTime(String keyboard, String word) {
        int count = 0;
        char[] wordArr = word.toCharArray();

        for (int i  = 0; i < wordArr.length; i++) {
            if (i == 0) count += keyboard.indexOf(wordArr[i]);
            else {
                count += (Math.abs(keyboard.indexOf(wordArr[(i-1)]) - keyboard.indexOf(wordArr[(i)])));
            }
        }
        return count;

    }
}