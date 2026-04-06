// Definition for a pair.
// type Pair struct {
//     Key   int
//     Value string
// }

func mergeSort(pairs []Pair) []Pair {

    if len(pairs) <= 1 {
        return pairs
    }

    temp := make([]Pair,len(pairs))
    mergeSortHelper(pairs, temp)
    return pairs
}

func mergeSortHelper(pairs, temp []Pair) {

    if len(pairs) <= 1 {return}

    mid := len(pairs) / 2

    mergeSortHelper(pairs[:mid], temp[:mid])
    mergeSortHelper(pairs[mid:], temp[mid:])

    left, right := 0, mid
    k := 0

    for left < mid && right < len(pairs) {

        if pairs[left].Key <= pairs[right].Key {
            temp[k] = pairs[left]
            left++
        } else {
            temp[k] = pairs[right]
            right++
        }
        k++
    }
    
    copy(temp[k:], pairs[left:mid])
    copy(temp[k:], pairs[right:])
    copy(pairs, temp)
}