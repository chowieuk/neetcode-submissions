/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

//  PseudoCode
//  create a dummy node, and a reference to it named tail
//  while list1 and list2 contain nodes
//    if the value of the node at list1 is less than that of list2:
    //  the next pointer of tail points to the node at list1
    //  advance the node at list1
    //  otherwise, do the same for list2
//    advance the tail pointer
//  if any nodes remain in a list, point the next tail to the node at that list
//  return dummy.next

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
    dummy := &ListNode{}
	tail := dummy

	for list1 != nil && list2 != nil {
		if list1.Val < list2.Val {
			tail.Next = list1
			list1 = list1.Next
		} else {
			tail.Next = list2
			list2 = list2.Next
		}
		tail = tail.Next
	}

	if list1 != nil {
		tail.Next = list1
	} else if list2 != nil {
		tail.Next = list2
	}
	return dummy.Next
}
