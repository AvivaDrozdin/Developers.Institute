#Problem Statement
# Given a list of numbers and a target, write a function to determine if the target can be calculated by summing together any 2 numbers in the list.
# The function should return True if the target can be calculated and False if not.

# For ease of analysis and to see whats going on, we will also print True and the 2 numbers, or False.




#Option 1 (Nested Loop / Brute) O(n^2)

def subsetsum(nums, target_num):

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target_num:
                print('True': nums[i], num[j])
                return True
    print('False')
    return False


#Option 2 (Presort / pointer - working from outside in) O(nlogn)

def subsetsum(nums, target_num):
    nums = sorted(nums)
    low = 0
    high = len(nums) - 1
    while low < high:
        if nums[low] + nums[high] == target_num:
            print('True': nums[low], nums[high])
            return True
        elif  (nums[low] < nums [high]) low += 1
        elif (nums[low] > nums [high]) low -= 1
    
    return False
       


#Option 3 (Hastable) O(n)
def subsetsum(nums, target_num):
    numset = set()

    for num in nums:
        if (target_num - num) in numset:
            print('True':)
            return True
        else:
            numset.add(num)
    return False



nums = [1, 6, -2, 100, -44 ]
