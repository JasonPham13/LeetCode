def containDuplicates(nums):
    my_Set = set()
    for i in nums:
        if i in my_Set:
            return True
        my_Set.add(i)
    return False
