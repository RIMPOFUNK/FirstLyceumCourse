num = '1'
nums1 = set()

while len(num) != 0:
    num = input()
    nums1.add(num)

num = input()
nums2 = set()
while len(num) != 0:
    nums2.add(num)
    num = input()

nums3 = nums1 & nums2

if len(nums3) == 0:
    print("EMPTY")
else:
    for i in nums3:
        print(i)