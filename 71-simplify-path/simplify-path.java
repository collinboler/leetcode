class Solution {
    public String simplifyPath(String path) {
        Stack<String> stack = new Stack<>();
        for (String dir : path.split("/")) {
            if (dir.isEmpty() || dir.equals (".")) {
                continue;
            }

            if (dir.equals("..")) {
                if (!stack.isEmpty()){
                    stack.pop();
                }
            }
            else stack.push(dir);

        }
       
        // return
        int i = stack.size();
        String[] result = new String[i];
        while (!stack.isEmpty()) {
            i--;
            result[i] = stack.pop();
        }
        StringBuilder sb = new StringBuilder();
        for (String s : result) {
            sb.append("/");
            sb.append(s);
        }
        if (sb.isEmpty()) return "/";
        return sb.toString();  
    }
}