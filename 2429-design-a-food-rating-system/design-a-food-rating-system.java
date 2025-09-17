class FoodItem implements Comparable<FoodItem> {
    String food;
    String cuisine;
    int rating;
    boolean isValid;

    FoodItem(String food, String cuisine, int rating) {
        this.food = food;
        this.cuisine = cuisine;
        this.rating = rating;
        this.isValid = true;
    }

    @Override
    public int compareTo(FoodItem other) {
        if (this.rating != other.rating) {
            return other.rating - this.rating; // reverse order
        } // lexicographical ordering
        return this.food.compareTo(other.food); // recursive?
    }

}

class FoodRatings {
    HashMap<String, PriorityQueue<FoodItem>> map; // cuisine, fooditem pq
    HashMap<String, FoodItem> foodMap; // food, fooditem
    HashMap<String, String> foodToCuisine; // food, cuisine


    public FoodRatings(String[] foods, String[] cuisines, int[] ratings) {
        map = new HashMap<>();
        foodMap = new HashMap<>();
        foodToCuisine = new HashMap<>();

        for (int i = 0; i < foods.length; i++) {
            FoodItem food = new FoodItem(foods[i], cuisines[i], ratings[i]);
            foodMap.put(foods[i], food); 
            foodToCuisine.put(foods[i], cuisines[i]); 
            if (map.get(cuisines[i]) == null) { // create new pq for cuisine if first
                PriorityQueue<FoodItem> pq = new PriorityQueue<>();
                map.put(cuisines[i], pq);
            }
            map.get(cuisines[i]).add(food);
        }
    }
    
    public void changeRating(String food, int newRating) {
        FoodItem oldF = foodMap.get(food);
        oldF.isValid = false;
        
        FoodItem newF = new FoodItem(food, foodToCuisine.get(food), newRating); // create new valid food 
        map.get(foodToCuisine.get(food)).add(newF); // add new valid food to pq
        foodMap.put(food, newF); // update map
    }
    
    public String highestRated(String cuisine) {
        PriorityQueue<FoodItem> pq = map.get(cuisine);
        while (!pq.peek().isValid) {
            pq.poll(); // clean inValid rating at top
        }
        return pq.peek().food;
    }
}

/**
 * Your FoodRatings object will be instantiated and called as such:
 * FoodRatings obj = new FoodRatings(foods, cuisines, ratings);
 * obj.changeRating(food,newRating);
 * String param_2 = obj.highestRated(cuisine);
 */