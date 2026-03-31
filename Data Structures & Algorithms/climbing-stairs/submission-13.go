
func Solution(n int, cache map[int]int) int {
    if n < 2 {
        cache[n] = 1
        return cache[n]
    }

    val, ok := cache [n]
    if ok {
        return val
    }

    cache[n] = Solution(n-1, cache) + Solution(n-2, cache)
    return cache[n]
}

func climbStairs(n int) int {
    
    return Solution(n, make(map[int]int))
}
