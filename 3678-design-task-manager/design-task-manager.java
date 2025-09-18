class Task implements Comparable<Task>{
    int userId;
    int taskId;
    int priority;
    boolean isValid;
    Task(int userId, int taskId, int priority) {
        this.userId = userId;
        this.taskId = taskId;
        this.priority = priority;
        this.isValid = true;
    }

    @Override
    public int compareTo(Task other){
        if (this.priority != other.priority) return other.priority - this.priority; // this is descending?
        

        if (this.taskId != other.taskId) return other.taskId - this.taskId;
        return other.userId - this.userId;
    }

}

class TaskManager {
    HashMap<Integer, Task> map; // task id, task
    PriorityQueue<Task> pq;
    public TaskManager(List<List<Integer>> tasks) {
        this.map = new HashMap<>();
        this.pq = new PriorityQueue<>();

        for (List<Integer> t : tasks) {
            Task task = new Task(t.get(0), t.get(1), t.get(2));
            map.put(t.get(1), task);
            pq.add(task);
        }
    }
    
    public void add(int userId, int taskId, int priority) {
        Task task = new Task(userId, taskId, priority);
        map.put(taskId, task); // overwrite old task with new task
        pq.add(task);
    }
    
    public void edit(int taskId, int newPriority) {
        map.get(taskId).isValid = false;
        Task task = new Task(map.get(taskId).userId, taskId, newPriority);
        map.put(taskId, task); // overwrite map value
        pq.add(task);
        
    }
    
    public void rmv(int taskId) {
        map.get(taskId).isValid = false;
        map.remove(taskId);
        
    }
    
    public int execTop() {
        if (pq.isEmpty()) return -1;
        while (pq.peek().isValid == false) {
            if (pq.size() - 1 == 0 ) return -1;
            pq.poll();
        }
        
        if (pq.isEmpty()) return -1;
        return pq.poll().userId;
    }
}

/**
 * Your TaskManager object will be instantiated and called as such:
 * TaskManager obj = new TaskManager(tasks);
 * obj.add(userId,taskId,priority);
 * obj.edit(taskId,newPriority);
 * obj.rmv(taskId);
 * int param_4 = obj.execTop();
 */