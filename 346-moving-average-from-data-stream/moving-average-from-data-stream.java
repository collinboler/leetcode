class MovingAverage {
    Queue<Integer> queue;
    int size;
    public MovingAverage(int size) {
        this.size = size;
        this.queue = new LinkedList<>();
    }
    
    public double next(int val) {
        if (queue.size() == 0) {
            queue.offer(val);
            return val;
        }
        else if (queue.size() < this.size) {
            int sum = 0;
            queue.offer(val);
            for (int i : queue) {
                sum += i;
            }
            return (double) sum / (double) queue.size();
        }
        else {
            int sum = 0;
            queue.poll();
            queue.offer(val);
            for (int i : queue) {
                sum += i;
            }
            return (double) sum / (double) queue.size();
        }
    }
}

/**
 * Your MovingAverage object will be instantiated and called as such:
 * MovingAverage obj = new MovingAverage(size);
 * double param_1 = obj.next(val);
 */