#
# class Slolution:
#     def smallestEqual(self,num: List[int]) -> int:
#         for i in range(len(num)):
#             if i % 10 == num[i]:
#                 return i
#
#         return -1


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
#         index_node = []
#         ind = 1
#         while head.next and head.next.next:
#             if (head.next.val > head.val and head.next.val > head.next.next.val) or (
#                     head.next.val < head.val and head.next.val < head.next.next.val):
#                 index_node.append(ind)
#                 ind += 1
#             else:
#                 ind += 1
#             head = head.next
#
#         if len(index_node) < 2:
#             return [-1, -1]
#         index_node.sort()
#         maxDis = index_node[-1] - index_node[0]
#         minDis = min([index_node[i + 1] - index_node[i] for i in range(len(index_node) - 1)])
#         return [minDis, maxDis]



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
#         l = []
#         while head:
#             l.append(head.val)
#             head = head.next
#         ans = []
#         if len(l) <= 3:
#             return [-1,-1]
#         for i in range(1,len(l) - 1):
#             if (l[i - 1] < l[i] and l[i + 1] < l[i]) or (l[i - 1] > l[i] and l[i + 1] > l[i]):
#                 ans.append(i)
#         if len(ans) < 2:
#             return [-1,-1]
#         ans.sort()
#         mind = math.inf
#         for i in range(len(ans) - 1):
#             mind = min(mind,ans[i + 1] - ans[i])
#         return [mind,ans[-1] - ans[0]]





class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        res, i, cur = [], 0, head.next
        while cur.next:
            if (head.val < cur.val and cur.val > cur.next.val) or (head.val > cur.val and cur.val < cur.next.val): res.append(i)
            head, cur, i = cur, cur.next, i + 1
        return [min(res[i + 1] - res[i] for i in range(len(res) - 1)), res[-1] - res[0]] if len(res) >= 2 else [-1, -1]



