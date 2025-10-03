class Solution {
    public int maxBottlesDrunk(int numBottles, int numExchange) {
        int count = numBottles; // drink all
        int empty = count; // num empty
        
        while (empty >= numExchange ) {
            count++;
            empty -=  numExchange - 1;
            numExchange++;
        }
          
        return count;
    }
}