'''

最容易想到的方法是枚举数组中的每一个数 x，寻找数组中是否存在 target - x。

当我们使用遍历整个数组的方式寻找 target - x 时，需要注意到每一个位于 x 之前的元素都已经和 x 匹配过，因此不需要再进行匹配。而每一个元素不能被使用两次，所以我们只需要在 x 后面的元素中寻找 target - x。


'''


class List:
    pass


class Solution:
    def twoSum(self,nums:List[int],target:int) -> List[int]:
        hashtable = dict()
        for i,num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num,i]]
            hashtable[nums[i]] = i
        return  []