/**
 * // This is the ImmutableListNode's API interface.
 * // You should not implement it, or speculate about its implementation.
 * interface ImmutableListNode {
 *     public void printValue(); // print the value of this node.
 *     public ImmutableListNode getNext(); // return the next node.
 * };
 */

class Solution {

    public void printLinkedListInReverse(ImmutableListNode head) {
        // brute force with stack
        // Stack<ImmutableListNode> stack = new Stack<>();
        // ImmutableListNode node = head;
        // while (node != null) {
        //     stack.push(node);
        //     node = node.getNext();
        // }
        // while (!stack.isEmpty()) {
        //     node = stack.pop();
        //     node.printValue();
        // }

        // recursive
        if (head != null) {
            printLinkedListInReverse(head.getNext());
            head.printValue();
        }


    }
}