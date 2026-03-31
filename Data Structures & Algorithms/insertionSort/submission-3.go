// Definition for a pair.
// type Pair struct {
//     Key   int
//     Value string
// }

func insertionSort(pairs []Pair) [][]Pair {
    result := make([][]Pair, 0)
    for i := range(pairs) {
        j := i - 1

        for j >= 0 && pairs[j].Key > pairs[j + 1].Key {
            pairs[j], pairs[j + 1] = pairs[j + 1], pairs[j]
            j--
        }

        clone := make([]Pair, len(pairs))
        copy(clone, pairs)
        result = append(result, clone)
    }
    return result
}
