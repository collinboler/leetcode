class Solution {
    public String makeGood(String s) {
        Stack<Character> stack = new Stack<>();
        if (s.length() == 0) return s;

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (!stack.isEmpty() && stack.peek() == Character.toUpperCase(c) && c != Character.toUpperCase(c)) {
                stack.pop();
            }
            else if (!stack.isEmpty() && stack.peek() == Character.toLowerCase(c) && c != Character.toLowerCase(c)) {
                stack.pop();
              
            }
            else stack.push(c);
        }
        StringBuilder sb = new StringBuilder();
        for (Character c : stack) {
            sb.append(c);
        }
        return sb.toString();    
}
}