
import (
    "slices"
)
/**
 * Definition of Interval:
 * type Interval struct {
 *    start int
 *    end   int
 * }
 */

func minMeetingRooms(intervals []Interval) int {

	if len(intervals) == 0 {
		return 0
	}

	starts := make([]int, len(intervals))
	ends := make([]int, len(intervals))

	for i, v := range intervals {

		starts[i] = v.start
		ends[i] = v.end
	}

	slices.Sort(starts)
	slices.Sort(ends)

	rooms := 0
	endIdx := 0

	for i := range len(starts) {

		if starts[i] < ends[endIdx] {
			rooms++

		} else {
			endIdx++
		}

	}

	return rooms
}
