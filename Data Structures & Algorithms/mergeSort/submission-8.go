// Definition for a pair.
// type Pair struct {
//     Key   int
//     Value string
// }

func merge(l, r, buf []Pair) []Pair {
    buf = buf[:0]

    i, j := 0, 0
    for i < len(l) && j < len(r) {
        if l[i].Key <= r[j].Key {
            buf = append(buf,l[i])
            i++
        } else {
            buf = append(buf, r[j])
            j++
        }
    }
    buf = append(buf, l[i:]...)
    buf = append(buf, r[j:]...)

    return buf
}

func mergeSortHelper(pairs, temp []Pair) {
    if len(pairs) <= 1 {
        return
    }

    mid := len(pairs) / 2

    mergeSortHelper(pairs[:mid], temp[:mid])
    mergeSortHelper(pairs[mid:], temp[mid:])

    merged := merge(pairs[:mid], pairs[mid:], temp[:len(pairs)])

    copy(pairs,merged)

}

func mergeSort(pairs []Pair) []Pair {
    temp := make([]Pair, len(pairs))
    mergeSortHelper(pairs, temp)
    return pairs
}
