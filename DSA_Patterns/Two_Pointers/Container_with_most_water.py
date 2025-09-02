class Solution:
    def maxArea(self, height):
        n = len(height)
        max_area = 0
        l = 0
        r = n-1

        while l < r:
            h = min(height[l], height[r])
            w = r - l
            area = h * w
            max_area = max(area, max_area)

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return max_area