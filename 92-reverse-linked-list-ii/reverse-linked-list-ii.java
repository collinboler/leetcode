/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        if (head.next == null) return head;
        ListNode dummy = new ListNode();
        dummy.next = head;
        ListNode prev = dummy; // behind head;
        for (int i = 1; i < left; i++) {
            prev = prev.next;
        }
        // curr = 2,3,4,5,6
        ListNode curr = prev.next;
        ListNode tail = curr;
        ListNode next = null;
   
        for (int i = 0; i < (right - left) + 1; i++) {    
            next = curr.next;
            curr.next = prev.next;
            
            prev.next = curr;
            curr = next;

        }
        tail.next = curr;
        return dummy.next;
        // tail.next = curr;
        // return head;
    }
    
  
}

