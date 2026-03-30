/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func reverseList(head *ListNode) *ListNode {

	// base case: head is null
	if head == nil {
		return nil
	}

	newHead := head
	if head.Next != nil {
		newHead = reverseList(head.Next)
		head.Next.Next = head
	}
	head.Next = nil

	return newHead
}
