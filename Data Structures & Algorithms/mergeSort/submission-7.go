// Definition for a pair.
// type Pair struct {
//     Key   int
//     Value string
// }

func mergeSort(pairs []Pair) []Pair {
    if len(pairs) <= 1 {
        return pairs
    }

    temp := make([]Pair, len(pairs))

    var sort func(start,end int)
    sort = func(start,end int) {
        if end - start <= 1 {
            return
        }

        mid := (start + end) / 2

        sort(start,mid)
        sort(mid, end)

        i,j := start, mid
        k := start

        for i < mid && j < end {
            if pairs[i].Key <= pairs[j].Key {
                temp[k] = pairs[i]
                i++
            } else {
                temp[k] = pairs[j]
                j++
            }
            k++
        }

        copy(temp[k:], pairs[i:mid])
        copy(temp[k:], pairs[j:end])
        copy(pairs[start:end],temp[start:end])
    }

    sort(0, len(pairs))

    return(pairs)
}
