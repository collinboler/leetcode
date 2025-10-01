class Solution {
    public int numWaterBottles(int numBottles, int numExchange) {
        int count = numBottles;
        int empty = count;
        
        while (empty >= numExchange ) {
            count += empty / numExchange;
            empty = empty % numExchange + (empty / numExchange);
        }
          
        return count;
    }

}