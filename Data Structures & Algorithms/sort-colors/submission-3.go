func sortColors(nums []int) {

    buckets := make([]int, 3)

    for _, v := range(nums) {
        buckets[v]++
    }

    i := 0
    for n := range(len(buckets)){
        for range(buckets[n]) {
            nums[i] = n
            i++
        }
    }
    
}
