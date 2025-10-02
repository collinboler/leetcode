class Solution {
    public int maxBottlesDrunk(int numBottles, int numExchange) {
        int drunk = numBottles; // total bottles drunk
        int empty = numBottles; // empty bottles after drinking initial ones
        
        while (empty >= numExchange) {
            // Exchange once
            empty -= numExchange;  // use up required empty bottles
            numExchange++;         // cost increases by 1
            drunk++;               // drink the new full bottle
            empty++;               // that bottle becomes empty
        }
        
        return drunk;
    }
}
