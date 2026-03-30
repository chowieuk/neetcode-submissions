// Bruteforce
func productExceptSelf(nums []int) []int {
    output := []int{}
    for i, _ := range(nums) {
        product := 1
        for j, v := range(nums) {
            if i == j {
                continue
            }
            product *= v
        }
        output = append(output, product)
    }
    return output
}
