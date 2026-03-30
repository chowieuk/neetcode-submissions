func isValid(s string) bool {
	if len(s)%2 != 0 {
		return false
	}

	// Using a byte slice instead of rune
	stack := make([]byte, 0)

	for i := 0; i < len(s); i++ {
		c := s[i]
		switch c {
		case '(', '{', '[':
			stack = append(stack, c)
		case ')', '}', ']':
			if len(stack) == 0 {
				return false
			}
			top := stack[len(stack)-1]
			
			// Map pairing checked via math/ascii relationships or explicit checks
			if (c == ')' && top != '(') || 
			   (c == '}' && top != '{') || 
			   (c == ']' && top != '[') {
				return false
			}
			stack = stack[:len(stack)-1]
		}
	}

	return len(stack) == 0
}