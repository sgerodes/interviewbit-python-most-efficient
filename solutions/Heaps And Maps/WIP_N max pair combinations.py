class Solution:
    # @param A : list of N integers
    # @param B : list of N integers
    # @return a list of integers

    # a O(n^2) solution. not optimal
    def solve(self, A, B):
        return sorted([a+b for a in A for b in B], reverse=True)[:len(A)]




if __name__ == '__main__':
    s = Solution().solve([ 3, 2, 4, 2], [4, 3, 1, 2])
    print(s)
    #[print(si) for si in s]