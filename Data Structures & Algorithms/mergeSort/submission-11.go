// Definition for a pair.
// type Pair struct {
//     Key   int
//     Value string
// }

func mergeSort(pairs []Pair) []Pair {

    if len(pairs) <= 1 {return pairs}

    buf := make([]Pair,len(pairs))

    mergeSortHelper(pairs, buf)

    return pairs
}

func mergeSortHelper(pairs, buf []Pair) {

    if len(pairs) <= 1 {return}

    mid := len(pairs) / 2

    mergeSortHelper(pairs[:mid],buf[:mid])
    mergeSortHelper(pairs[mid:],buf[mid:])

    i, j := 0, mid
    k := 0

    for i < mid && j < len(pairs) {
        if pairs[i].Key <= pairs[j].Key {
            buf[k] = pairs[i]
            i++
        } else {
            buf[k] = pairs[j]
            j++
        }
        k++
    }

    copy(buf[k:], pairs[i:mid])
    copy(buf[k:], pairs[j:])
    copy(pairs, buf)
}
