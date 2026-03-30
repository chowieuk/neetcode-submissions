type MyStack struct {
	q []int
}

func Constructor() MyStack {
	return MyStack{}
}

func (ms *MyStack) Push(x int) {
    ms.q = append(ms.q, x)
}

func (ms *MyStack) Pop() int {
    lastIndex := len(ms.q) - 1
    last := ms.q[lastIndex]
    ms.q = ms.q[:lastIndex]
    return last
}

func (ms *MyStack) Top() int {
    return ms.q[len(ms.q) - 1]
}

func (ms *MyStack) Empty() bool {
    return len(ms.q) == 0
}
