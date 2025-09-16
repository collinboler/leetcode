class Solution {

    public static int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    public static long lcm(int a, int b) {
        return ((long) a * b) / gcd(a, b);
    }

    public static boolean coprime(int a, int b) { return gcd(a,b) == 1;}
    public List<Integer> replaceNonCoprimes(int[] nums) {
        List<Integer> list = new ArrayList<>();
        for (int num : nums) {
            list.add(num);
        }

        for (int i = 0; i < list.size() - 1; i++) {
            if (!coprime(list.get(i), list.get(i + 1))) {
                long newVal = lcm(list.get(i), list.get(i + 1));
         
                list.remove(i + 1);
                list.set(i, (int)newVal);
                if (i > 0) i -= 2;
                else i--;
            }
        } 
        return list;
    }
}