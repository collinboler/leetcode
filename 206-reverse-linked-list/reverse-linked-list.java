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
    public ListNode reverseList(ListNode head) {
       ListNode prev = null;
       ListNode curr = head;
       while (curr != null) {
            ListNode nextNode = curr.next; // store real next node
            curr.next = prev;               // overwrite real next node with previous node
            prev = curr;                    // overwrite previous placeholder node with current node
            curr = nextNode;                // set curr = to the real next node and continue traversing the list
       }
        return prev;

    }
}