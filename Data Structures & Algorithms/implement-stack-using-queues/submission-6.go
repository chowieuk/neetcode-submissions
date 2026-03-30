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
    i := len(ms.q) - 1
    v := ms.q[i]
    ms.q = ms.q[:i]
    return v
}

func (ms *MyStack) Top() int {
    return ms.q[len(ms.q) - 1]
}

func (ms *MyStack) Empty() bool {
    return len(ms.q) == 0
}
