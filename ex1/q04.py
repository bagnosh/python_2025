import sys
nums = []
for line in sys.stdin:
    nums.append(float(line))
for i in reversed(nums):
    print(i," ")