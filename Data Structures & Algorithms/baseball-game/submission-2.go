func calPoints(operations []string) int {
	stack := []int{}
	for _, v := range operations {
		switch v {
		case "+":
			stack = append(stack, (stack[len(stack)-1] + stack[len(stack)-2]))
		case "D":
			stack = append(stack, stack[len(stack)-1] * 2)
		case "C":
			stack = stack[:len(stack)-1]
		default:
		    val, _ := strconv.Atoi(v)
			stack = append(stack, val)
		}
	}
	sum := 0
	for _, v := range stack {
		sum += v
	}

	return sum

}
