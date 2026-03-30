func productExceptSelf(nums []int) []int {
    n := len(nums)
    output := make([]int, n)

    // Forward pass: calculate prefix products
    lp := 1
    for i := range nums {
        output[i] = lp
        lp *= nums[i]
    }

    // Backward pass: calculate suffix products and multiply
    rp := 1
    for i := range nums {
        rev := n - 1 - i // Calculate the backward index
        
        output[rev] *= rp
        rp *= nums[rev]
    }

    return output
}