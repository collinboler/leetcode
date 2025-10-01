class Solution {
    int empty;
    public int numWaterBottles(int numBottles, int numExchange) {
        int count = numBottles;
        empty = count;
        
        while (empty >= numExchange ) {
            count += empty / numExchange;
            empty = empty % numExchange + (empty / numExchange);
        }
          
        return count;
    }

}