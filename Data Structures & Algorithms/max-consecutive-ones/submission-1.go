func findMaxConsecutiveOnes(nums []int) int {
    res, cnt := 0, 0
	for _, n := range nums {
        if n == 1 {
            cnt++
        } else {
            cnt = 0
        }
        res = max(cnt,res)
    }
    return res
}
