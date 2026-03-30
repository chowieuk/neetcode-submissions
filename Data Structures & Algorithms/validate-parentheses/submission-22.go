func isValid(s string) bool {
	stack := []rune{}
	closeToOpen := map[rune]rune{')': '(', ']': '[', '}': '{'}

	for _, c := range s {
		if v, ok := closeToOpen[c]; ok {
			if len(stack) != 0 && stack[len(stack)-1] == v {
				stack = stack[:len(stack)-1]
			} else {
				return false
			}
		} else {
			stack = append(stack, c)
		}
	}
	if len(stack) == 0 {
		return true
	} else {
		return false
	}
}