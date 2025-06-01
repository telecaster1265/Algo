import sys

input = sys.stdin.readline

nums = []
for _ in range(5):
    num = int(input())
    nums.append(num)

avg = sum(nums) // 5
nums.sort()
mid = nums[2]

print(avg)
print(mid)