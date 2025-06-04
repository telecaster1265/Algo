import sys

input = sys.stdin.readline

n = int(input())
nums = []
for _ in range(n):
    num = int(input())
    nums.append(num)
mean = round(sum(nums) / n)

nums.sort()
median = nums[n // 2]

f = {}
for num in nums:
    if num in f:
        f[num] += 1
    else:
        f[num] = 1
max_f = max(f.values())
modes = []
for key, value in f.items():
    if value == max_f:
        modes.append(key)

modes.sort()
mode = modes[1] if len(modes) > 1 else modes[0]

r = nums[-1] - nums[0]

print(mean)
print(median)
print(mode)
print(r)