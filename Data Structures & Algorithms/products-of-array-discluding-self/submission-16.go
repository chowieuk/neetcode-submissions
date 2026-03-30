func productExceptSelf(nums []int) []int {
    output := make([]int, len(nums))

    // Forward pass: calculate prefix products
    lp := 1
    for i := range nums {
        output[i] = lp
        lp *= nums[i]
    }

    // Backward pass: calculate suffix products and multiply
    rp := 1
    for i := range nums {
        rev := len(nums) - 1 - i // Calculate the backward index
        
        output[rev] *= rp
        rp *= nums[rev]
    }

    return output
}