// Definition for a pair.
// type Pair struct {
//     Key   int
//     Value string
// }

func QuickSort(pairs []Pair) []Pair {

    QuickSortHelper(pairs, 0, len(pairs) - 1)

    return pairs

}

func QuickSortHelper(arr []Pair, s, e int){

    if e - s + 1 < 1 {
        return 
    }

    pivot := arr[e]
    left := s

    for i := s; i < e; i++ {
        if arr[i].Key < pivot.Key {
            arr[left], arr[i] = arr[i], arr[left]
            left++
            }
    }

    arr[e] = arr[left]
    arr[left] = pivot
    

    QuickSortHelper(arr, s, left - 1)
    QuickSortHelper(arr, left + 1, e)

}
