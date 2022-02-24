/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public var val: Int
 *     public var next: ListNode?
 *     public init() { self.val = 0; self.next = nil; }
 *     public init(_ val: Int) { self.val = val; self.next = nil; }
 *     public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }
 * }
 */
public class ListNode {
    public var val: Int
    public var next: ListNode?
    public init() { self.val = 0; self.next = nil; }
    public init(_ val: Int) { self.val = val; self.next = nil; }
    public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }
}
class Solution {
    func mergeNodes(_ head: ListNode?) -> ListNode? {
        var node = head
        while node?.next != nil {
            if node?.next?.next == nil {
                node?.next = nil
            }
            else if node?.next?.val == 0 {
                node = node?.next
            }
            else {
                node?.val = (node?.next?.val ?? 0) + (node?.val ?? 0)
                node?.next = node?.next?.next
            }
        }
        return head
    }
}
