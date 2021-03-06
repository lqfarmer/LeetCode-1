"""
题号 454 四数相加II
给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[l] = 0。

为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。所有整数的范围在 -228 到 228 - 1 之间，最终结果不会超过 231 - 1 。

例如:

输入:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

输出:
2

解释:
两个元组如下:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0



"""
from typing import List

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        count = 0
        ab_map = {}
        for a in A:
            for b in B:
                ab_map[a+b] = ab_map.get(a+b, 0)+1
        for c in C:
            for d in D:
                s = -(c+d)
                if s in ab_map:
                    count += ab_map[s]
        return count

    # 两行代码
    def fourSumCount2(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        from collections import Counter
        counter = Counter([a + b for a in A for b in B])
        return sum([counter[-(c+d)] for c in C for d in D])

if __name__ == '__main__':
    A = [1, 2]
    B = [-2, -1]
    C = [-1, 2]
    D = [0, 2]

    solution = Solution()
    print(solution.fourSumCount2(A,B,C,D))
