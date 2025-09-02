class Solution:
    def twoSum(self, numbers, target):
        n = len(numbers)

        left = 0
        right = n-1

        while left < right:
            summ = numbers[left] + numbers[right]
            if summ == target:
                return [left+1, right+1]
            elif summ < target:
                left += 1
            else:
                right -= 1
        return [-1, -1]
    
