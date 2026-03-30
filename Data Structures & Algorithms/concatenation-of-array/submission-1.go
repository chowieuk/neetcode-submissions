func getConcatenation(nums []int) []int {
	ans := make([]int, len(nums)*2)
	copy(ans,nums)
	copy(ans[len(nums):],nums)
	return ans
}
