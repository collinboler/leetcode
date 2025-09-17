
class FoodItem {
    String food;
    String cuisine;
    int rating; 
    
    public FoodItem(String food, int rating, String cuisine) {
        this.food = food;
        this.rating = rating;
        this.cuisine = cuisine;
    }
}
class FoodRatings {
    
    HashMap<String, PriorityQueue<FoodItem>> map;
    HashMap<String, String> foodmap;
    HashMap<String, FoodItem> foodToItem;
    
    public FoodRatings(String[] foods, String[] cuisines, int[] ratings) {
        this.map = new HashMap<>();
        this.foodmap = new HashMap<>();
        this.foodToItem = new HashMap<>();
        for (int i = 0; i < foods.length; i++) {
            foodmap.put(foods[i], cuisines[i]);
            FoodItem food = new FoodItem(foods[i], ratings[i], cuisines[i]);
            // create new cuisine queue if needed
            if (!map.containsKey(cuisines[i])) {
                map.put(cuisines[i], new PriorityQueue<>(
                Comparator.comparingInt((FoodItem f) -> f.rating).reversed().thenComparing(f -> f.food)
            ));
            } 
            map.get(cuisines[i]).add(food);
            foodToItem.put(foods[i], food);
        }
    }
    
    public void changeRating(String food, int newRating) {
        String cuisine = foodmap.get(food);
        FoodItem oldf = foodToItem.get(food);
        foodToItem.remove(food);

        PriorityQueue<FoodItem> pq = map.get(cuisine);
        pq.remove(oldf);
        
        FoodItem newF = new FoodItem(food, newRating, cuisine);
        pq.add(newF);
        foodToItem.put(food, newF);

    }
    
    public String highestRated(String cuisine) {
        FoodItem bestFood = this.map.get(cuisine).peek();
        return bestFood.food;
    }


}

/**
 * Your FoodRatings object will be instantiated and called as such:
 * FoodRatings obj = new FoodRatings(foods, cuisines, ratings);
 * obj.changeRating(food,newRating);
 * String param_2 = obj.highestRated(cuisine);
 */