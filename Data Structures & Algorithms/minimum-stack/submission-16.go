type MinStack struct {
	stack    []int
	minStack []int
}

func Constructor() MinStack {
	stack := make([]int, 0)
	minStack := make([]int, 0)

	return MinStack{
		stack: stack,
		minStack: minStack,
	}
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

    m.stack = m.stack[:len(m.stack) - 1]
    m.minStack = m.minStack[:len(m.minStack) - 1]
}

func (m *MinStack) Top() int {
    return m.stack[len(m.stack) - 1]
}

func (m *MinStack) GetMin() int {
    return m.minStack[len(m.minStack) - 1]

}
