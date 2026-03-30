type MinStack struct {
	stack    []int
	minStack []int
}

func Constructor() MinStack {
	return MinStack{}
}

func (m *MinStack) Push(val int) {
    m.stack = append(m.stack, val)
    if len(m.minStack) == 0 {
        m.minStack = append(m.minStack, val)
    } else {
        lastIndex := len(m.minStack) - 1
        m.minStack = append(m.minStack, min(m.minStack[lastIndex], val))
    }
}

func (m *MinStack) Pop() {
    lastIndex := len(m.stack) - 1
    m.stack = m.stack[:lastIndex]
    m.minStack = m.minStack[:lastIndex]
}

func (m *MinStack) Top() int {
    lastIndex := len(m.stack) - 1
    return m.stack[lastIndex]
}

func (m *MinStack) GetMin() int {
    lastIndex := len(m.minStack) - 1
    return m.minStack[lastIndex]

}
