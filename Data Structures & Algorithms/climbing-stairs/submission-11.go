func climbStairs(n int) int {
    var dfs func(i int) int
    cache := make(map[int]int)

    dfs = func(i int) int {
        if i >= n {
            if i == n {
                return 1
            }
            return 0
        }
        if val, exists := cache[i]; exists {
            return val
        }

        val1, exists := cache[i + 1]
        if !exists {
            val1 = dfs(i + 1)
        }

        val2, exists := cache[i + 2]
        if !exists {
            val2 = dfs(i + 2)
        }

        result := val1 + val2
        cache[i] = result
        return result
    }
    return dfs(0)
}