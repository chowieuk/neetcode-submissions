// Definition for a pair.
// type Pair struct {
//     Key   int
//     Value string
// }

func merge(l, r []Pair) []Pair {
	res := make([]Pair, 0, len(l)+len(r))
	i, j := 0, 0

	for i < len(l) && j < len(r) {
		if l[i].Key <= r[j].Key {
			res = append(res, l[i])
            i++
		} else {
			res = append(res, r[j])
            j++
		}
	}

	if i == len(l) {
		res = append(res, r[j:]...)
	} else {
		res = append(res, l[i:]...)
	}

	return res
}

func mergeSort(pairs []Pair) []Pair {

	if len(pairs) <= 1 {
		return pairs
	}

	m := len(pairs) / 2

	L := mergeSort(pairs[:m])
	R := mergeSort(pairs[m:])
	return merge(L, R)
}
