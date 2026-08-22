class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sortedNums = sorted(nums)
        current = None
        maxStreak = 0
        streak = 0

        print(sortedNums)
        for n in sortedNums:
            if current is None:
                streak += 1
            else:
                if current + 1 == n:
                    streak += 1
                elif current == n:
                    continue
                else:
                    if streak > maxStreak:
                        maxStreak = streak
                    streak = 1
            current = n 
        if streak > maxStreak:
            maxStreak = streak
        return maxStreak

            