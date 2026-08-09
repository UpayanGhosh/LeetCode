# Last updated: 10/08/2026, 02:36:41
class Solution(object):
    def spiralOrder(self, matrix):
        ans = []
        while matrix:
            #1) Appennd all the elements of the first row in the result matrix
            ans += (matrix.pop(0))

            #2) Append the last elements of all the lists in proper order
            if matrix and matrix[0]:
                for row in matrix:
                    ans.append(row.pop()) # Remember if you donot mention any index in pop it will always pop the last element
            #3) Append the remaining elements of the last row inn reverse order
            if matrix:
                ans += (matrix.pop()[::-1]) # Poping the last row for example one will be (7,8) but we want (8,7) so we reversed it
            #4) Append first element of all the rows in reverse order
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    ans.append(row.pop(0))
        return ans
        