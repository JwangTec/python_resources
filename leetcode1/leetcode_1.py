# class Solution:
#     def reverse(self, x: int) -> int:
#         str1 = str(x)
#         str2 = ''
#         if x >= 0:
#
#                 str2 += str1[i]
#         else:
#             a = -x
#             str1 = str(a)
#             str2 = "-"
#             for i in range(len(str1)-1,-1,-1):
#                 str2 += str1[i]
#         if -(2**31) <= int(str2) <= (2**31 -1):
#             return int(str2)
#         else:
#             return 0
#
#
# s1 = Solution()
# aa = s1.reverse(-1232300)
# print(aa)

#
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         str1 = str(x)
#         if str1 == str1[::-1]:
#             return True
#         else:
#             return False
#
# a1 = Solution()
#
#
# print(a1.isPalindrome(12321))