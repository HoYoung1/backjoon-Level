N = int(input())
nums = [0]*26
i = 0
while i < N:
    for j, c in enumerate(input()[::-1]):
        nums[ord(c)-ord('A')] += (10**j)
    i += 1
nums.sort(reverse=True)
result = 0
for i in range(10):
    if nums[i]:
        result += (nums[i] * (9-i))
print(result)