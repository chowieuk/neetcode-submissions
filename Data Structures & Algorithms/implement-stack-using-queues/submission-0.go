
type MyStack struct {
	list *list.List
}

func Constructor() MyStack {
	l := list.New()
	return MyStack{
		list: l,
	}
}

func (ms *MyStack) Push(x int) {
    ms.list.PushFront(x)
}

func (ms *MyStack) Pop() int {
    front := ms.list.Front()
    return ms.list.Remove(front).(int)
}

func (ms *MyStack) Top() int {
    if front := ms.list.Front(); front != nil {
        return front.Value.(int)
    } else {
        return -1
    }
}

func (ms *MyStack) Empty() bool {
    return ms.list.Len() == 0 
}
