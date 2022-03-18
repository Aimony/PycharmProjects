# class Solution:
#     def findWord(self,word: List[str]) -> List[str]:
#         ans = []
#         rowIdx = "122101110111220000100202020"
#         for word in words:
#             idx = rowIdx[ord(word[0].lower()) - ord('a')]
#             if all(rowIdx[ord(ch.lower()] - ord('a')] == idx for ch in word):
#                 ans.append(word)
#         return ans