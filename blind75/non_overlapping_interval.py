class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # step 1: Sort by end time (this sort by 2nd element in the array [start, end])
        intervals.sort(key=lambda x: x[1])

        count_inter_removed = 0
        prev_end = intervals[0][1]


        # step 2:  iterate through the first intervals
        for start, end in intervals[1:]:
            if start < prev_end:
                # Overlap - remove this interval and count
                count_inter_removed +=1
            else:
                # No Overlap - keep it
                prev_end = end

       return  count_inter_removed


# how the lambda function works in python in the greedy algorithm
# it is used to Order intervals so the one that finishes earliest comes first, so greedy can work.

# def get_end_time(x): # x = [start, end]
#     return x[1] # x[1] = end
# therefore, the sort is sorting the list using the key, which is returning the end time in order of the smallest value.