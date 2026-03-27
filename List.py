List
nums = [1, 2, 3, 4, 5]
print(nums)
print("Length:", len(nums))
#adding element
nums.append(6)
print(nums)
#Removing element 
nums.remove(3)
print(nums)
#Finding element
if 2 in nums:
    print("Found")
else:
    print("Not Found")

#printing largest value
print("Largest:", max(nums))
