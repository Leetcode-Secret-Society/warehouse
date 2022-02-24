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
        var result = [Int]()
        var count = 0
        while node?.next != nil {
//            print("\(node?.val)-\(count)")
            if node?.val == 0 {
                if count != 0 {
                    result.append(count)
                }
                count = 0
            } else {
                count += node?.val ?? 0
            }
            node = node?.next
        }
        if count != 0 {
            result.append(count)
        }
        
//        print(result)
        var resultNode : ListNode?
        var resultNodeTmp : ListNode?
        for theVal in result {
            let theNode = ListNode.init(theVal)
            if resultNode == nil {
                resultNode = theNode
            }
            resultNodeTmp?.next = theNode
            resultNodeTmp = theNode
        }
        return resultNode
    }
}
