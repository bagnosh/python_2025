import sys
nums = []
for line in sys.stdin:
    try:
        num = float(line)
        nums.append(num)
    except ValueError:
        break
if not nums:
    print("Oops, no values!")
else:
    biggest = max(nums)
    print(f"Max value: {biggest}")