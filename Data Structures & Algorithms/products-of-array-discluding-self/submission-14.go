// Suffix product, Prefix product
func productExceptSelf(nums []int) []int {
    output := make([]int, len(nums))
    for i := range(len(nums)){
        output[i] = 1
    }

    for i := 1; i < len(nums); i++ {
        output[i] = output[i-1] * nums[i-1]
    }

    rp := 1
    for i := len(nums) - 1; i >= 0; i-- {
        output[i] = output[i] * rp
        rp = rp * nums[i]
    }

    return output
}
