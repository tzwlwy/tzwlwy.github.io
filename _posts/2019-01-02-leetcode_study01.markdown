---
layout: post
category: "leetcode"
title:  "leetcode题目学习 "
header-img: "img/in-post/post-bg-unix-linux.jpg"
tags:
    - leetcode
---


**题目  sum和  **
```python
'''
给定一个整数数组，返回两个数字的索引，使它们相加到特定目标。

您可以假设每个输入只有一个解决方案，并且您可能不会两次使用相同的元素。
例如：
鉴于nums = [2,7,11,15]，target = 9，

因为nums [ 0 ] + nums [ 1 ] = 2 + 7 = 9，
返回[ 0，1 ]
'''

#答案
class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i

Given_nums =[3,2,  11,7, 15,9]
target = 9
s=Solution().twoSum(Given_nums,target)
print(s)
```